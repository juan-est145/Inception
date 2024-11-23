#!/usr/bin/python3
import subprocess
import shutil
import os

if os.path.exists("/var/www/html/myWebsite"):
    shutil.rmtree("/var/www/html/myWebsite", ignore_errors=True)
shutil.move("/root/myWebsite", "/var/www/html")

command = (
    "openssl req -x509 -nodes -days 365 -newkey rsa:2048 "
    "-keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt "
    "-subj \"/C=ES/L=Madrid/O=42Malaga/OU=student/CN=juestrel.42.fr\""
)

subprocess.run(command, shell=True, executable="/bin/bash")
subprocess.run(["nginx", "-g", "daemon off;"])