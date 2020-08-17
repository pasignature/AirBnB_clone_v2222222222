#!/usr/bin/python3
""" cleans archieves used to deploy to servers """
from fabric.api import *


env.hosts = ['34.75.27.131', '34.73.20.109']
env.user = "ubuntu"


def do_clean(number=0):
    """ clean archieves """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
