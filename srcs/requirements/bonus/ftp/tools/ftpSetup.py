#!/usr/bin/python3
import os
import subprocess

os.system(f"echo '/bin/false' >> /etc/shells")
os.system(f"adduser {os.getenv('MY_FTPUSER')} --shell /bin/false --home /home/{os.getenv('MY_FTPUSER')} --disabled-password")
os.system(f"echo '{os.getenv('MY_FTPUSER')}:{os.getenv('MY_FTPPASSWORD')}' | chpasswd")

os.system(f"addgroup {os.getenv('SERVER_GROUP')}")
os.system(f"adduser --disabled-password --gecos '' --ingroup {os.getenv('SERVER_GROUP')} {os.getenv('SERVER_USER')}")
os.system(f"addgroup {os.getenv('ANON_GROUP')}")
os.system(f"adduser --disabled-password --gecos '' --ingroup {os.getenv('ANON_GROUP')} {os.getenv('ANON_USER')}")

os.system(f"chown -R {os.getenv('ANON_USER')}:{os.getenv('ANON_GROUP')} /var/proftpd/wordpress/wp-content")
os.system(f"chmod -R 755 /var/proftpd/wordpress/wp-content")
subprocess.run(["/usr/sbin/proftpd", "-nc","/etc/proftpd/conf.d/proftpd.conf"])