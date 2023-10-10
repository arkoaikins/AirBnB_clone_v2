#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive(compress) from the conents
of the web_static,this helps to compress files before sending to server
for deployment
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the contents of web_static
    Returns:The archive path if created correctly else return None
    """
    try:
        local("mkdir -p versions")    
        # create the time for the archive files
        arc_time = datetime.now().strftime('%Y%m%d%H%M%S')

        # create the compressed file 
        arc_path = "versions/web_static_{}.tgz".format(arc_time)
        local("tar -czvf {} web_static".format(arc_path))
        # check if the archive was correctly generated
        if local("test -e {}".format(arc_path), capture=True):

            return arc_path 
        else:
            return None
    except Exception as e:
        pass
