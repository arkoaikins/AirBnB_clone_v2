#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
import os

env.hosts = ['54.90.14.86', '54.160.114.180']


def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py) that
    distributes an archive to your web servers.

    Returns:
        True if all operations have been done correctly, else return False
    """
    # Check if the archive file exists locally
    if not os.path.exists(archive_path):
        return False
    try:
        # Get the filename from the archive_path
        arc_file = os.path.basename(archive_path)
        # Create a directory with the archive filename without the extension
        arc_dir = arc_file.split(".")[0]
        # Folder on the webserver
        serv_fld = "/data/web_static/releases/"
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')
        # Uncompress the archive to a folder on the web server
        run('mkdir -p {}{}/'.format(serv_fld, arc_dir))
        run('tar -xzf /tmp/{} -C {}{}/'.format(arc_file, serv_fld, arc_dir))
        # Delete the archive from the web server
        run('rm /tmp/{}'.format(arc_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(serv_fld, arc_dir))
        # Delete the symbolic link /data/web_static/current from the web server
        run('rm -rf {}{}/web_static'.format(serv_fld, arc_dir))
        run('rm -rf /data/web_static/current')
        # Create a new symbolic link /data/web_static/current
        run('ln -s {}{}/ /data/web_static/current'.format(serv_fld, arc_dir))
        print("New version deployed!")
        return True
    except Exception:
        return False
