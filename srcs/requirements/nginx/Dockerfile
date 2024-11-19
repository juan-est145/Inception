FROM debian:bullseye

RUN apt-get update -y && apt-get install nginx -y && apt-get install openssl -y && apt-get install -y python3

COPY tools/index.html /usr/share/nginx/html
COPY conf/default /etc/nginx/sites-available/default
COPY tools/nginxSetup.py /usr/local/bin

RUN chmod +x /usr/local/bin/nginxSetup.py

EXPOSE 443/tcp

CMD ["nginxSetup.py"]