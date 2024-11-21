#!/usr/bin/python3
import os
import urllib.request as request

def setConfigFile(path: str):
	with open(path) as file:
		configFile = file.read()
	configFile = configFile.replace("database_name_here", os.getenv("DB_NAME"))
	configFile = configFile.replace("username_here", os.getenv("DB_USER"))
	configFile = configFile.replace("password_here", os.getenv("DB_PASSWORD"))
	configFile = configFile.replace("localhost", f"{os.getenv('DB_HOSTNAME')}:{os.getenv('DB_PORT')}")
	with open(path, "w") as file:
		file.write(configFile)

if not os.path.exists("/var/www/html"):
	os.makedirs("/var/www/html")
response = request.urlopen("https://wordpress.org/latest.tar.gz")
with open("/tmp/latest.tar.gz", "wb") as file:
    file.write(response.read())
os.system("tar -xzvf /tmp/latest.tar.gz -C /var/www/html")
configFilePath = "/var/www/html/wordpress"
os.rename(f"{configFilePath}/wp-config-sample.php", f"{configFilePath}/wp-config.php")
setConfigFile(f"{configFilePath}/wp-config.php")
while 1:
	1