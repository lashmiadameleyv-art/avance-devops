import boto3
from datetime import datetime, timedelta

# --- CONFIGURACIÓN PRINCIPAL ---
REGION = 'us-east-1'
NOMBRE_ASG = 'GrupoAutoescalado-DevOps' # El nombre exacto que está en tu YAML

# Inicializamos los clientes
ec2 = boto3.client('ec2', region_name=REGION)
cloudwatch = boto3.client('cloudwatch', region_name=REGION)
s3 = boto3.client('s3', region_name=REGION)
autoscaling = boto3.client('autoscaling', region_name=REGION)

def listar_instancias_ec2():
    print("\n[EC2] Listando instancias en la cuenta...")
    respuesta = ec2.describe_instances()
    instancia_activa = None
    
    for reservacion in respuesta['Reservations']:
        for instancia in reservacion['Instances']:
            id_inst = instancia['InstanceId']
            estado = instancia['State']['Name']
            print(f"  -> ID: {id_inst} | Estado: {estado}")
            
            # Guardamos la primera instancia que esté corriendo para sacarle las métricas
            if estado == 'running' and not instancia_activa:
                instancia_activa = id_inst
                
    return instancia_activa

def obtener_metricas_cpu(instance_id):
    if not instance_id:
        print("\n[CloudWatch] No se encontró ninguna instancia en estado 'running' para medir.")
        return
        
    print(f"\n[CloudWatch] Obteniendo CPU de la instancia activa: {instance_id}")
    tiempo_fin = datetime.utcnow()
    tiempo_inicio = tiempo_fin - timedelta(hours=1)
    
    respuesta = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2', 
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=tiempo_inicio, 
        EndTime=tiempo_fin,
        Period=300, 
        Statistics=['Average']
    )
    
    puntos = respuesta.get('Datapoints', [])
    if not puntos:
        print("  -> No hay datos recientes (la instancia es muy nueva o no tiene carga).")
    else:
        for p in sorted(puntos, key=lambda x: x['Timestamp']):
            print(f"  -> {p['Timestamp']} | CPU: {p['Average']:.2f}%")

def listar_s3():
    print("\n[S3] Listando Buckets...")
    respuesta = s3.list_buckets()
    buckets = respuesta.get('Buckets', [])
    if not buckets:
        print("  -> No se encontraron buckets.")
    for bucket in buckets:
        print(f"  📦 Bucket: {bucket['Name']}")

def gestionar_autoescalado(nombre_grupo):
    print(f"\n[AutoScaling] Configurando política para el grupo: {nombre_grupo}")
    try:
        autoscaling.put_scaling_policy(
            AutoScalingGroupName=nombre_grupo,
            PolicyName='EscaladoPorCPU-Proyecto',
            PolicyType='TargetTrackingScaling',
            TargetTrackingConfiguration={
                'PredefinedMetricSpecification': {'PredefinedMetricType': 'ASGAverageCPUUtilization'},
                'TargetValue': 70.0
            }
        )
        print("  -> ✅ Política de autoescalado aplicada con éxito al grupo.")
    except Exception as e:
        print(f"  -> Error (¿Ya se ejecutó el archivo YAML para crear el grupo?): {e}")

if __name__ == "__main__":
    listar_s3()
    
    # 1. Lista las instancias y detecta el ID automáticamente
    id_instancia_encontrada = listar_instancias_ec2()
    
    # 2. Usa ese ID para sacar las métricas
    obtener_metricas_cpu(id_instancia_encontrada)
    
    # 3. Aplica la regla al grupo de autoescalado
    gestionar_autoescalado(NOMBRE_ASG)
    
    print("\n🚀 ¡Tareas de automatización finalizadas exitosamente!")
