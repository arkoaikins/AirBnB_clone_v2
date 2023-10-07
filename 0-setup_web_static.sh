#!/usr/bin/env bash
# Prepare your web servers

# Install Nginx
# apt-get -y purge nginx nginx-common
# apt-get -y autoremove
apt-get --assume-yes update
apt-get --assume-yes install nginx
ufw allow 'Nginx HTTP'

# Folders
mkdir --parents /data/

# Ownership
chown --recursive "$USER":"$USER" /data/

mkdir --parents /data/web_static/
mkdir --parents /data/web_static/releases/
mkdir --parents /data/web_static/shared/
mkdir --parents /data/web_static/releases/test/

# Fake HTML file
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html


# Link
web_current=/data/web_static/current
test_dir=/data/web_static/releases/test/

if [ -e "$web_current" ]; then
	rm --force "$web_current"
fi
ln --symbolic "$test_dir" "$web_current"

# Update Nginx configuration
nginx_conf=/etc/nginx/sites-enabled/default

# shellcheck disable=SC2016
echo '# Configuration for server - ONWUTA EBUBE GIDEON
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	# Add index
	index index.html

	server_name _;

	location /hbnb_static {
		# Select directory
		alias /data/web_static/current/;
		autoindex off;
	}

	location / {
		# First attempt to serve a request as file, then
		# as directiory, then fall back to dispalying a 404 ERROR.
		try_files $uri $uri/ =404;
	}
}' > "$nginx_conf"


# Upload changes
service nginx restart
