FROM debian:bullseye

RUN apt-get update -y && apt-get install -y python3 php php-fpm wget tar
COPY ./tools/wordpressSetup.py /usr/local/bin
RUN chmod +x /usr/local/bin/wordpressSetup.py

CMD ["wordpressSetup.py"]