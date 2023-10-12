#!/usr/bin/python3
"""
Fabric script that distributes an archive to webservers
"""
import os
from fabric.api import env, run, put, cd

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

    # Get the filename from the archive_path
    arc_file = os.path.basename(archive_path)

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, "/tmp/{}".format(arc_file))

    # Create a directory with the archive filename without the extension
    arc_dir = arc_file[:-4]

    # Uncompress the archive to a folder on the web server
    with cd('/data/web_static/releases'):
        run("mkdir -p {}".format(arc_dir))
        with cd('/tmp'):
            run("tar -xzf {} -C /data/web_static/releases/{}/".format(arc_file, arc_dir))

    # Delete the archive from the web server
    run("rm /tmp/{}".format(arc_file))

    # Delete the symbolic link /data/web_static/current from the web server
    with cd('/data/web_static'):
        run("rm current", warn_only=True)

    # Create a new symbolic link /data/web_static/current
    with cd('/data/web_static/releases'):
        run("ln -s {} /data/web_static/current".format(arc_dir))

    # Return True if all operations have been done correctly
    return True
