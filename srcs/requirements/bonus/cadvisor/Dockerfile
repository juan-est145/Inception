FROM debian:bullseye

RUN apt-get update -y && apt-get install -y wget
RUN wget https://github.com/google/cadvisor/releases/download/v0.49.1/cadvisor-v0.49.1-linux-amd64
RUN chmod +x cadvisor-v0.49.1-linux-amd64

EXPOSE 8080

CMD ["./cadvisor-v0.49.1-linux-amd64"]
