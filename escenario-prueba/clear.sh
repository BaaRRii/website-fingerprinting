#!/bin/bash

COMPOSE_FILE="docker-compose.yml"

echo "Deteniendo y eliminando el escenario de Docker Compose..."
docker-compose -f "$COMPOSE_FILE" down

if [ $? -eq 0 ]; then
  echo "Escenario detenido y eliminado correctamente."
  echo ""
  echo "Puedes volver a iniciarlo con el script 'start_scenario.sh'."
else
  echo "Error al detener y/o eliminar el escenario."
fi