#!/usr/bin/python3
# script that deletes out-of-date archives, using the function do_clean

from fabric.api import env, run, local
import os

env.hosts = ['54.90.14.86', '54.160.114.180']


def do_clean(number=0):
    """
    deletes out-of-date archives
    """
    number = int(number)

    if number == 0 or number == 1:
        number = 1
    else:
        number += 1

    local("ls -1t versions/ | tail -n +{} | \
            xargs -I {{}} rm versions/{{}}".format(number))
    run("ls -1t /data/web_static/releases/ | tail -n +{} | \
            xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(
                number))
