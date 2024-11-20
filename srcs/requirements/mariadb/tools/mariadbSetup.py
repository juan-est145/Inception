#!/usr/bin/python3
import os

def setConfigFile(path : str):
	with open(path, "r") as file:
		read = file.read()
	replace = read.replace("bind-address            = 127.0.0.1", "bind-address            = 0.0.0.0")
	with open(path, "w") as file:
		file.write(replace)

# Replace later user, db and password with envs'

mariaExec = "mariadb -e "
db = f"CREATE DATABASE IF NOT EXISTS db"
user = f"CREATE USER IF NOT EXISTS 'user'@'%' IDENTIFIED BY 'password'"
privileges = f"GRANT ALL ON db.* TO 'user'@'%';"
flush = "FLUSH PRIVILEGES;"

os.system(f"service mariadb start")
os.system(f"mariadb -e \"{db}\"")
os.system(f"mariadb -e \"{user}\"")
os.system(f"mariadb -e \"{privileges}\"")
os.system(f"mariadb -e \"{flush}\"")
setConfigFile("/etc/mysql/mariadb.conf.d/50-server.cnf")
os.system(f"mysqladmin -u root shutdown")
os.system(f"mysqld --port=3306 --user=root")