#!/usr/bin/python3
import subprocess
import http.client
import urllib.request as request

def getFile(url: str, path :str):
	response : http.client.HTTPResponse = request.urlopen(url)
	with open(path, "wb") as file:
		file.write(response.read())

getFile("https://github.com/vrana/adminer/releases/download/v4.8.1/adminer-4.8.1.php", "/var/www/html/index.php")

subprocess.run(["php", "-S", "0.0.0.0:8080", "-t", "/var/www/html"])