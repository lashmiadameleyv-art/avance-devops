import boto3
import json
from datetime import datetime, timedelta

# configuramos todo con mucha calma para la región permitida
region = 'us-east-1'
ec2_client = boto3.client('ec2', region_name=region)
s3_client = boto3.client('s3', region_name=region)
cw_client = boto3.client('cloudwatch', region_name=region)
dynamo_resource = boto3.resource('dynamodb', region_name=region)

def listar_recursos():
    print("buscando tus instancias ec2...")
    instancias = ec2_client.describe_instances()
    for reservacion in instancias['Reservations']:
        for inst in reservacion['Instances']:
            print(f"- instancia: {inst['InstanceId']}, estado: {inst['State']['Name']}")

    print("\nbuscando tus buckets de s3...")
    buckets = s3_client.list_buckets()
    for bucket in buckets['Buckets']:
        print(f"- bucket: {bucket['Name']}")

def obtener_metricas_cpu(instance_id):
    print(f"\nrevisando la salud de tu instancia {instance_id}...")
    respuesta = cw_client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=datetime.utcnow() - timedelta(hours=1),
        EndTime=datetime.utcnow(),
        Period=3600,
        Statistics=['Average']
    )
    for punto in respuesta['Datapoints']:
        print(f"- uso promedio de cpu: {punto['Average']}%")

def gestionar_dynamodb():
    print("\nconectando con tu base de datos dynamodb...")
    tabla_nombre = 'TablaFinanciera'

    tabla = dynamo_resource.Table(tabla_nombre)
    
    # insertar registro
    tabla.put_item(Item={'id': '1', 'mensaje': 'operación exitosa', 'estado': 'activo'})
    print("- registro insertado suavemente.")

if __name__ == '__main__':
    print("iniciando las tareas de automatización...\n")
    listar_recursos()
