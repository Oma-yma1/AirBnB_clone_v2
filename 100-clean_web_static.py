#!/usr/bin/python3
"""clean function"""
from fabric.api import *


env.hosts = ['100.25.33.169', '3.83.18.68']
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
