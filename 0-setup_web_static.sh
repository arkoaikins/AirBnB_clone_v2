#!/usr/bin/env bash
# Prepare your web servers

# Install Nginx
# apt-get -y purge nginx nginx-common
# apt-get -y autoremove
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'

# Folders
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

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

if [ -L "$web_current" ]; then
	# rm --recursive "$web_current";
	ln --symbolic --force "$test_dir" "$web_current"
else
	ln --symbolic --force "$test_dir" "$web_current"
fi

# Ownership
chown -R "$USER":"$USER" /data/

# Update Nginx configuration
nginx_conf=/etc/nginx/sites-enabled/default

# shellcheck disable=SC2016
printf %s '# Configuration for server - ONWUTA EBUBE GIDEON
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

	location /redirect_me {
		# Have fun with redirection
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	# Create a custom 404 error page
	error_page 404 /404.html;
	location = /404.html {
		# to ensure it cannot be accessed directly by clients
		internal;
	}
}' > "$nginx_conf"


# Upload changes
service nginx restart
