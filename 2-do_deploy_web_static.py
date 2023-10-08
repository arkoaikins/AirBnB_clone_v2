#!/usr/bin/python3
"""
Deploy archive to web servers
"""
from fabric.api import *
from os.path import isfile

env.hosts = ['18.207.2.78', '54.162.43.21']


def do_deploy(archive_path):
    """
    Deploy this archive to the specific web servers
    """
    if not isfile(archive_path):
        # print("File not found")
        return False

    # print("type: {} | val = {}".format(type(archive_path), archive_path))

    # Get name for unzipped file
    archive = archive_path.split(sep="versions/")[1]
    unzipped = archive.split(sep=".tgz")[0]
    # print("Unzipped: {}".format(unzipped))

    # Upload archive
    run("mkdir --parents /tmp/")
    put(local_path=archive_path, remote_path="/tmp/")

    # Uncompress archive
    cmd = "mkdir --parents /data/web_static/releases/{}/".format(unzipped)
    run(cmd)

    cmd = "tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
    cmd = cmd.format(archive, unzipped)
    run(cmd)

    # remove temporary file
    cmd = "rm /tmp/{}".format(archive)
    run(cmd)
    cmd = "mv /data/web_static/releases/{}/web_static/*".format(unzipped)
    cmd = cmd + " /data/web_static/releases/{}/".format(unzipped)
    run(cmd)

    cmd = "rm -rf /data/web_static/releases/{}/web_static".format(unzipped)
    run(cmd)

    # Relink deployed code
    run("rm -rf /data/web_static/current")
    cmd = "ln -s /data/web_static/releases/{}/".format(unzipped)
    cmd = cmd + " /data/web_static/current"
    run(cmd)

    # Confirmation
    # print("New version deployed!")
    return True
