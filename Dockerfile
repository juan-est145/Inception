FROM debian:bullseye

RUN apt-get update -y && apt-get install nginx -y && apt-get install openssl -y && apt-get install -y python3

COPY index.html /usr/share/nginx/html
COPY default /etc/nginx/sites-available/default
COPY nginxSetup.py /usr/local/bin

RUN chmod +x /usr/local/bin/nginxSetup.py

EXPOSE 443/tcp

CMD ["nginxSetup.py"]