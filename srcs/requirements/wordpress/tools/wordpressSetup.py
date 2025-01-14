#!/usr/bin/python3
import os
import urllib.request as request
import http.client
import shutil
import subprocess

def setConfigFile(path: str, keyValue : dict):
	with open(path) as file:
		configFile = file.read()
	for key, value in keyValue.items():
		configFile = configFile.replace(key, value)
	with open(path, "w") as file:
		file.write(configFile)

def getFile(url: str, path :str):
	response : http.client.HTTPResponse = request.urlopen(url)
	with open(path, "wb") as file:
		file.write(response.read())

if not os.path.exists("/var/www/html"):
	os.makedirs("/var/www/html")
if not os.path.exists("/run/php"):
	os.makedirs("/run/php")

# We download the wordpress files and set them up along with phpfm
getFile("https://wordpress.org/latest.tar.gz", "/tmp/latest.tar.gz")
os.system("tar -xzvf /tmp/latest.tar.gz -C /var/www/html")
configFilePath = "/var/www/html/wordpress"
os.system("chown -R www-data:www-data /var/www/html/wordpress")
os.rename(f"{configFilePath}/wp-config-sample.php", f"{configFilePath}/wp-config.php")
setConfigFile("/etc/php/7.4/fpm/pool.d/www.conf", {
	"listen = /run/php/php7.4-fpm.sock" : "listen = 0.0.0.0:9000"
})
setConfigFile(f"{configFilePath}/wp-config.php", {
	"database_name_here" : os.getenv("DB_NAME"),
	"username_here" : os.getenv("DB_USER"),
	"password_here" : os.getenv("DB_PASSWORD"),
	"localhost" : f"{os.getenv('DB_HOSTNAME')}:{os.getenv('DB_PORT')}",
	"/* That's all, stop editing! Happy publishing. */": f"define('WP_REDIS_HOST', {os.getenv('RD_HOST')});\ndefine('WP_REDIS_PORT', {os.getenv('RD_PORT')});",
})

# We install the wordpress cli to help with the installation
getFile("https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar", "wp-cli.phar")
os.chmod("wp-cli.phar", 755)
shutil.move("wp-cli.phar", "/usr/local/bin")

# Finally we create the admin and a user to the website with the cli
os.system(f"wp-cli.phar core install --allow-root --url={os.getenv('URL')} --title=\"Inception\"\
   --admin_user={os.getenv('WP_ADMIN')} --admin_password={os.getenv('WP_ADMIN_PASS')} \
   --admin_email={os.getenv('WP_ADMIN_EMAIL')} --skip-email --path={configFilePath}")
os.system(f"wp-cli.phar user create --allow-root {os.getenv('WP_USER')} {os.getenv('WP_USER_EMAIL')} --user_pass={os.getenv('WP_USER_PASS')}\
   --path=/var/www/html/wordpress --url={os.getenv('URL')}")

# We install the redis plugin
os.system(f"wp-cli.phar plugin install redis-cache --activate --allow-root --path=/var/www/html/wordpress")
os.system(f"wp-cli.phar plugin update --all --allow-root --path=/var/www/html/wordpress")
os.system(f"wp-cli.phar redis enable --allow-root --path=/var/www/html/wordpress")

subprocess.run(["php-fpm7.4", "-F"])