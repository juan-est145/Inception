# Inception

A repository containing the Inception project of 42 Malaga. The aim of this project is to contenaraize several services in different docker
containers and creating a local virtual network for them, WITHOUT using pre-made images from Docker Hub (except for the Os image). The three main services are a mariaDB database, a NGINX server and Wordpress website. 

As a bonus you can also add Adminer for administering the database, a Redis cache for the wordpress site, your own static website aside from the wordpress one, a FTP server of your liking that allows to download files from the Wordpress website and lastly, whatever service that you think that might be useful (in my case I chose cadvisor).

## Dependencies
In order to run this project you will need to have installed docker-engine and the make tool. If make is not available to your OS, you may use docker compose instead directly on the docker-compose.yml file.

Also, you will need to provide your .env file and place it inside the srcs folder. You will need to provide values the following keys.

```bash
  # MariaDB
DB_USER="Your value here"
DB_NAME="Your value here"
DB_PASSWORD="Your value here"
DB_PORT="Your value here"
DB_HOSTNAME="Your value here"

# Wordpress
URL="Your value here"
WP_TITLE="Your value here"
WP_ADMIN="Your value here"
WP_ADMIN_PASS="Your value here"
WP_ADMIN_EMAIL="Your value here"
WP_USER="Your value here"
WP_USER_EMAIL="Your value here"
WP_USER_PASS="Your value here"

# REDIS
RD_HOST="Your value here"
RD_PORT="Your value here"

# FTP
SERVER_USER= "Your value here"
SERVER_GROUP= "Your value here"
ANON_USER= "ftp"
ANON_GROUP= "Your value here"
MY_FTPUSER= "Your value here"
MY_FTPPASSWORD= "Your value here"
```

Lastly, if you want to access the websites through the url that you configure in the .env, you should set the dns record on the /etc/hosts file. Else, just access them through localhost.


## Run Locally

Clone the project

```bash
  git clone https://github.com/juan-est145/Inception.git
```

Go to the project directory

```bash
  cd Inception
```

Start the containers
```bash
  make
```

Alternatively, if you do not have make, you can use instead
```bash
  docker compose -f ./srcs/docker-compose.yml up -d --build
```

To stop the containers run 
```bash
  make down
```

Or use this instead if you do not have make
```bash
  docker compose -f ./srcs/docker-compose.yml down
```
