FROM debian:bullseye

RUN apt-get update -y && apt-get install -y wget php php-cli php-mysqli python3
RUN mkdir -p /var/www/html

COPY ./tools/adminerSetup.py /usr/local/bin
RUN chmod +x /usr/local/bin/adminerSetup.py

EXPOSE 8080

CMD ["adminerSetup.py"]