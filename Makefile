DOCKER = docker compose
YML_ROUTE = ./srcs/docker-compose.yml

all:
	mkdir -p ${HOME}/data/wordpress
	mkdir -p ${HOME}/data/dbData
	mkdir -p ${HOME}/data/redis
	$(DOCKER) -f $(YML_ROUTE) up -d --build

down:
	$(DOCKER) -f $(YML_ROUTE) down