#!/usr/bin/python3
"""clean function"""
from fabric.api import *


env.hosts = ['34.232.76.67', '54.224.49.219']
env.user = "ubuntu"


def do_clean(number=0):
    """function clean"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
