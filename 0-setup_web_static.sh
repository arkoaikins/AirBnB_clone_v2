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
chown --recursive ubuntu:ubuntu /data/

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
chown --recursive ubuntu:ubuntu "$web_current"


# Update Nginx configuration
nginx_conf=/etc/nginx/sites-enabled/default

default_index='/var/www/html/index.html'
SITE='/var/www/html'
error_page="$SITE/404.html"

mkdir --parents "$SITE"
chown --recursive ubuntu:ubuntu "$SITE"

printf "Hello World!\n" > "$default_index"
printf "Ceci n'est pas une page\n" > "$error_page"

# shellcheck disable=SC2016
echo '# Configuration for server - ONWUTA EBUBE GIDEON
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	# Include header in response
	add_header X-Served-By $hostname;

	# Add index
	index index.html

	server_name _;

	location / {
		# First attempt to serve a request as file, then
		# as directiory, then fall back to dispalying a 404 ERROR.
		try_files $uri $uri/ =404;
	}

	location /hbnb_static {
		# Select directory
		alias /data/web_static/current/;
		autoindex off;
	}

	location /redirect_me {
		# Have fun with redirection
		return 301 https://www/youtube.com/watch?v=QH2-TGUlw4;
	}

	# Create a custome 404 error page
	error_page 404 /404.html;
	location = /404.html {
		# to ensure it cannot be accessed directly by clients
		internal;
	}

}' > "$nginx_conf"


# Upload changes
service nginx restart
