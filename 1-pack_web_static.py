#!/usr/bin/python3
"""
Compress static web page
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Compress web_static directory
    """
    time = datetime.now()
    archive = "web_static_{}{}{}{}{}{}.tgz"
    archive = archive.format(time.year, time.month,
                             time.day, time.hour, time.minute, time.second)
    # print("Name for archive: {}".format(archive))

    # Create archive in the directory - versions
    to_be_archived = "web_static"
    local("mkdir --parents versions")
    cmd = "tar --create --gzip --verbose --file versions/{} {}"
    # cmd = "tar -cvzf versions/{} {}"
    cmd = cmd.format(archive, to_be_archived)
    local(cmd)
