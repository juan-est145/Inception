FROM debian:bullseye

RUN apt-get update -y && apt-get install -y proftpd python3

COPY ./conf/proftpd.conf /etc/proftpd/conf.d
COPY ./tools/ftpSetup.py /usr/local/bin

RUN mkdir -p /var/proftpd && chmod +x /usr/local/bin/ftpSetup.py

EXPOSE 21

CMD ["ftpSetup.py"]