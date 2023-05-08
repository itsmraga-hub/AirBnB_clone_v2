#!/usr/bin/env bash
# A bash script that sets up my web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt install -y nginx

sudo ufw allow 'Nginx HTTP'

#sudo systemctl restart nginx

sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
sudo echo "Hello World, Release Test Index.html" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx start
