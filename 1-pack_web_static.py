#!/usr/bin/python3
"""Compress before sending task"""
from fabric.api import local
from time import strftime


def do_pack():
    """generates .tgz archive from contents of the web_static"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(
                strftime("%Y%m%d%H%M%S")))
    except:
        return None
