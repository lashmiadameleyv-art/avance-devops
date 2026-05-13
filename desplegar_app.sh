#!/bin/bash
# desplegar_app.sh
# este script trae tu aplicación y la levanta suavemente con docker

echo "iniciando el proceso con calma..."

# 1. definimos dónde guardaremos la app y cuál es su origen
DIRECTORIO_APP="./app_desplegada"


URL_REPO_APP="https://github.com/RoySanchez111/CSS_Equipo3.git

# 2. limpiamos el espacio si es necesario, para que todo esté ordenado
if [ -d "$DIRECTORIO_APP" ]; then
  echo "limpiando el espacio de trabajo anterior..."
  rm -rf "$DIRECTORIO_APP"
fi

# 3. clonamos el repositorio de tu app
echo "trayendo el código de tu aplicación..."
git clone "$URL_REPO_APP" "$DIRECTORIO_APP"

# 4. entramos a la carpeta de la app y encendemos todo
echo "preparando los contenedores..."
cd "$DIRECTORIO_APP" || exit

# le damos permisos a tu script de espera por si la base de datos lo necesita
chmod +x wait-for-db.sh

# construimos y levantamos los servicios en segundo plano
docker-compose up --build -d

echo "¡listo! tu aplicación está corriendo tranquila y segura."
