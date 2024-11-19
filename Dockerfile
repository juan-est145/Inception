FROM debian:bullseye

RUN apt-get update -y && apt-get install nginx -y

COPY default /etc/nginx/sites-available/default

EXPOSE 80/tcp

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]