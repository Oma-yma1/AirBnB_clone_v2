#!/usr/bin/python3
""" creates and distributes an archive to your web serversusing deploy"""
from fabric.api import local, env, put, run
from time import strftime
import os.path
env.hosts = ['100.25.33.169', '3.83.18.68']


def do_pack():
    """function and store th path o created archive"""
    nw = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filnme = "versions/web_static_{}.tgz".format(nw)
        local("tar -cvzf {} web_static/".format(filnme))
        return filnme
    except ValueError:
        return None


def do_deploy(archive_path):
    """function, using the new path of the nw archive"""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filnme = archive_path.split("/")[-1]
        nm = filnme.split(".")[0]
        path_nm = "/data/web_static/releases/{}/".format(nm)
        link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_nm))
        run("tar -xzf /tmp/{} -C {}".format(filnme, path_nm))
        run("rm /tmp/{}".format(filnme))
        run("mv {}web_static/* {}".format(path_nm, path_nm))
        run("rm -rf {}web_static".format(path_nm))
        run("rm -rf {}".format(link))
        run("ln -s {} {}".format(path_nm, link))
        return True
    except ValueError:
        return False


def deploy():
    """createand distribute archives to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    done = do_deploy(archive_path)
    return done


def do_clean(number=0):
    """function clean"""
    if number == 0:
        number = 1
    with cd.local('./versions'):
        local("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
            xargs -d '\n' rm".format(1 + number))
    with cd('/data/web_static/releases/'):
        run("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
            xargs -d '\n' rm".format(1 + number))
