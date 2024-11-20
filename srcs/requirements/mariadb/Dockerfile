FROM debian:bullseye

RUN apt-get update -y && apt-get install mariadb-server python3 -y
COPY tools/mariadbSetup.py /usr/local/bin
RUN chmod +x /usr/local/bin/mariadbSetup.py


CMD ["mariadbSetup.py"]