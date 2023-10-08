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
    if run("mkdir --parents /tmp/").failed is True:
        return False

    if put(local_path=archive_path, remote_path="/tmp/").failed is True:
        return False

    # Uncompress archive
    cmd = "mkdir --parents /data/web_static/releases/{}/".format(unzipped)
    if run(cmd).failed is True:
        return False

    cmd = "tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
    cmd = cmd.format(archive, unzipped)
    if run(cmd).failed is True:
        return False

    # remove temporary file
    cmd = "rm --force /tmp/{}".format(archive)
    if run(cmd).failed is True:
        return False

    cmd = "mv -f /data/web_static/releases/{}/web_static/*".format(unzipped)
    cmd = cmd + " /data/web_static/releases/{}/".format(unzipped)
    if run(cmd).failed is True:
        return False

    cmd = "rm -rf /data/web_static/releases/{}/web_static".format(unzipped)
    if run(cmd).failed is True:
        return False

    # Relink deployed code
    if run("rm -rf /data/web_static/current").failed is True:
        return False

    cmd = "ln -sf /data/web_static/releases/{}/".format(unzipped)
    cmd = cmd + " /data/web_static/current"
    if run(cmd).failed is True:
        return False

    # Confirmation
    print("New version deployed!")
    return True
