#!/usr/bin/python3
"""distribute archive toweb servers"""
from fabric.api import env, put, run
import os.path
env.hosts = ['100.25.33.169', '3.83.18.68']


def do_deploy(archive_path):
    """distribute the  archive to web serverusing do_deploy"""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        arcv_fl = archive_path.split("/")[-1]
        fl_nm = arcv_fl.split(".")[0]
        nw_vrs = "/data/web_static/releases/{}/".format(fl_nm)
        link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(nw_vrs))
        run("tar -xzf /tmp/{} -C {} --strip-components=1".format(arcv_fl, nw_vrs))
        run("rm /tmp/{}".format(arcv_fl))
        run("rm -rf {}*".format(nw_vrs))
        run("rm -rf {}".format(link))
        run("ln -s {} {}".format(nw_vrs, link))
        return True
    except ValueError:
        return False
