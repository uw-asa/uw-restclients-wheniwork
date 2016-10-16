import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wheniwork_restclient',
    version='0.1',
    packages=['wheniwork_restclient'],
    include_package_data=True,
    install_requires = [
        'setuptools',
        'Django<=1.8.6',
        'urllib3',
        'certifi',
    ],
    license='Apache License, Version 2.0',  # example license
    description='A Django app for consuming the WhenIWork REST API',
    long_description=README,
)
