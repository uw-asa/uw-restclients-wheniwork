from setuptools import find_packages, setup

setup(
    name='wheniwork_restclient',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'UW-RestClients-Core>0.8',
        'urllib3',
        'python-dateutil',
    ],
    license='Apache License, Version 2.0',
    description='A Django app for consuming the WhenIWork REST API',
    long_description='README.md',
)
