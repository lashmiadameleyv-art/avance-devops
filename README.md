# Proyecto Final DevOps en AWS  
## Automatización de despliegue, monitoreo y seguridad para aplicaciones web financieras

## 📌 Descripción General

Este proyecto fue desarrollado como solución al caso de análisis de la empresa **Soluciones Tecnológicas del Futuro**, organización enfocada en el desarrollo de aplicaciones web para el sector financiero.

Actualmente, la empresa enfrenta problemas operativos debido a procesos manuales de despliegue, retrasos en actualizaciones, errores en producción y poca visibilidad del rendimiento de sus aplicaciones.

Como respuesta, se diseñó e implementó una arquitectura basada en principios **DevOps**, utilizando servicios de AWS y herramientas modernas de automatización, integración continua, monitoreo y seguridad.

---

## 🎯 Objetivo del Proyecto

Diseñar e implementar un flujo de trabajo DevOps eficiente y escalable que permita:

- Automatizar despliegues de software
- Reducir errores manuales
- Mejorar tiempos de entrega
- Incrementar estabilidad operativa
- Monitorear infraestructura en tiempo real
- Aplicar controles de seguridad bajo enfoque DevSecOps
- Facilitar colaboración entre desarrollo y operaciones

---

## 🧩 Principios DevOps Aplicados

### 🔹 Automatización
Se automatizaron tareas repetitivas mediante:

- Scripts Bash
- Scripts Python
- Docker
- AWS CloudFormation
- AWS CodePipeline
- AWS Systems Manager

### 🔹 Integración y colaboración
Se implementó flujo colaborativo con:

- GitHub
- Branching strategy (`main` / `develop`)
- Pull Requests
- Revisión de cambios
- Buenas prácticas Agile

### 🔹 Integración Continua / Entrega Continua (CI/CD)

Pipeline automatizado con:

- AWS CodeCommit / GitHub
- AWS CodeBuild
- AWS CodePipeline

### 🔹 Monitoreo y medición

Uso de:

- AWS CloudWatch
- Dashboards personalizados
- Alarmas automáticas
- Logs centralizados

### 🔹 Seguridad (DevSecOps)

Controles implementados mediante:

- IAM Roles (LabRole)
- Security Groups
- Escaneo de vulnerabilidades (SonarQube propuesto)
- Acceso restringido por red
- Cifrado de datos en S3

---

# 🛠 Tecnologías Utilizadas

- Git & GitHub
- AWS EC2
- AWS Cloud9
- AWS CloudFormation
- AWS CodePipeline
- AWS CodeBuild
- AWS Systems Manager
- AWS Lambda
- AWS API Gateway
- AWS CloudWatch
- AWS Config
- AWS S3
- AWS DynamoDB
- Docker
- Docker Compose
- Python (boto3)
- Bash scripting
- Linux Ubuntu

---

# 📂 Gestión de Código Fuente

Repositorio privado configurado en GitHub con:

- Protección de rama `main`
- Rama `develop`
- Pull Requests obligatorios
- Convenciones de commits:

```bash
feat:
fix:
docs:
refactor:
## Actualización del proyecto finaly DevOps AWS
