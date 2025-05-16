FROM nginx:latest
RUN apt-get update && apt-get install -y iproute2
RUN apt-get install -y iputils-ping ethtool
COPY html /usr/share/nginx/html
EXPOSE 80
EXPOSE 443