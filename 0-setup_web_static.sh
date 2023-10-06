#!/usr/bin/env bash
# Prepare your web servers

# Install Nginx
apt-get -y purge nginx nginx-common
apt-get -y autoremove
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
	rm --recursive "$web_current";
	ln --symbolic "$test_dir" "$web_current"
else
	ln --symbolic "$test_dir" "$web_current"
fi

# Ownership
chown -R "$USER":"$USER" /data/

# Update Nginx configuration
nginx_conf=/etc/nginx/sites-enabled/default

old_string="server_name _;"
new_string="server_name _;\n\n\tlocation /hbnb_static/ {\n\t\t# project location\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n"

sed -i "/$old_string/c$new_string" "$nginx_conf"

# Upload changes
service nginx restart
