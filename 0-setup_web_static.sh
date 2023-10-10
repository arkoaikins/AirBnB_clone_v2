#!/usr/bin/env bash
# Scipt that prepare webservers and creates a fake Html
# to test the Nginx configuration

# install nginx if not already installed
if [  ! "$(command -v nginx)" ]; then
	sudo apt-get update
	sudo apt install nginx -y
fi

# create the directory /data/web_static/releases/test/ if it doesnt't already exist
folder="/data/web_static/releases/test/"
if [ ! -d "$folder" ]; then
	mkdir -p "$folder"
fi

# create the directory /data/web_static/shared/ if it doesn't already exist
sec_folder="/data/web_static/shared/"
if [ ! -d "$sec_folder" ]; then
	mkdir -p "$sec_folder"
fi

# create a fake html file(index.html) to test the nginx config
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link /data/web_static/current linked to the
# /data/web_static/releases/test/ folder,if the symbolic link aleady
# exists,it should be deleted and recreated
sym_link="/data/web_static/current"
linked_to="/data/web_static/releases/test/"

if [ -L "$sym_link" ]; then
	rm "$sym_link"
fi

ln -sf "$linked_to" "$sym_link"

# Give ownership of /data/ to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update nginx configuration to serve the content of $sym_link using alias
sudo sed -i '66 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

# Restart nginx to effect changes
sudo service nginx restart


