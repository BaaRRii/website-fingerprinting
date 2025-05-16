# Usa una imagen base minimalista de Ubuntu
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y iproute2
RUN apt-get install -y iputils-ping ethtool

# Actualiza el sistema e instala dependencias básicas, incluyendo Google Chrome
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    curl \
    unzip \
    gnupg \
    tcpdump \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Instalar Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable

# Instalar librerías de Python necesarias
RUN pip3 install selenium==4.15.2 pyshark pandas webdriver_manager scapy

# Copiar los scripts en el contenedor
WORKDIR /app
RUN mkdir -p /app/pcaps
COPY . /app

# Ejecutar el script de captura (puedes usar entrypoint.sh o directamente ejecutar el script)
# CMD ["python3", "capture_script.py"]
