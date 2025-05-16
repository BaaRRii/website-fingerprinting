#!/bin/bash

COMPOSE_FILE="docker-compose.yml"

echo "Iniciando el escenario con Docker Compose..."

if [[ "$@" == *"--build"* ]]; then
  echo "Reconstruyendo las imágenes..."
  docker-compose -f "$COMPOSE_FILE" up -d --build servidor router cliente
else
  docker-compose -f "$COMPOSE_FILE" up -d servidor router cliente
fi

if [ $? -eq 0 ]; then
  echo "Escenario iniciado correctamente."
  echo ""
  echo "Puedes acceder a los contenedores con:"
  echo "  docker exec -it escenario-prueba_servidor_1 /bin/bash"
  echo "  docker exec -it escenario-prueba_router_1 /bin/bash"
  echo "  docker exec -it escenario-prueba_cliente_1 /bin/bash"
  echo ""
else
  echo "Error al iniciar el escenario."
fi