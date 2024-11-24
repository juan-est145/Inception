FROM debian:bullseye

RUN apt-get update -y && apt-get install -y redis-server
COPY ./conf/redis.conf /etc/redis/redis.conf
EXPOSE 6379

CMD ["redis-server", "/etc/redis/redis.conf"]