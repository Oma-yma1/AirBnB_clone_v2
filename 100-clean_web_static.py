#!/usr/bin/python3
"""clean function"""
from fabric.api import *


env.hosts = ['100.25.33.169', '3.83.18.68']
env.user = "ubuntu"


def do_clean(number=0):
    """functinclean"""
    number = int(number)

    if number == 0 or number == 1:
        number = 1
    else:
        number += 1

    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs rm -f'.format(number))

    pat = '/data/web_static/releases'
    with cd(pat):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number))
