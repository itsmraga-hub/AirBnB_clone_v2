#!/usr/bin/env bash
# A bash script that sets up my web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt install -y nginx

sudo ufw allow 'Nginx HTTP'

#sudo systemctl restart nginx
sudo service nginx start

sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
sudo echo "Hello World, Release Test Index.html" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/


sudo sed -i '/server {/a location /hbnb_static {\nalias /data/web_static/current/;\n}' /etc/nginx/sites-available/default


sudo nginx -t

if [ $? -eq 0 ]; then
	sudo systemctl reload nginx
else
	exit 1
fi
