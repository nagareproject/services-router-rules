# Encoding: utf-8

# --
# Copyright (c) 2008-2021 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from os import path

from setuptools import setup, find_packages


here = path.normpath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as long_description:
    LONG_DESCRIPTION = long_description.read()

setup(
    name='nagare-services-router-rules',
    author='Net-ng',
    author_email='alain.poirier@net-ng.com',
    description='REST url router',
    long_description=LONG_DESCRIPTION,
    license='BSD',
    keywords='',
    url='https://github.com/nagareproject/services-router-rules',
    packages=find_packages(),
    zip_safe=False,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=[
        'webob', 'nagare-peak-rules',
        'nagare-services', 'nagare-server-http'
    ],
    entry_points='''
        [nagare.services]
        router = nagare.services.router_rules:Router
    '''
)
