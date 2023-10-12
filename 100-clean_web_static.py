from fabric.api import env, run, local
import os

"""
script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean
"""
env.hosts = ['54.90.14.86', '54.160.114.180']


def do_clean(number=0):
    """
    deletes out-of-date archives
    """
    if number == 0:
        number = 1
    try:
        number = int(number)
        local("ls -1t versions/ | tail -n +{} | \
              xargs -I {{}} rm versions/{{}}".format(number + 1))
        run("ls -1t /data/web_static/releases/ | tail -n +{} | \
              xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(
                  number + 1))
    except ValueError:
        pass
