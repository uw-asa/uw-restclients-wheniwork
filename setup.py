from setuptools import setup, find_packages
setup(
    name='wheniwork_restclient',
    version='0.1',
    packages=find_packages(),
    install_requires = [
        'Django',
        'urllib3',
        'certifi',
        'python-dateutil',
    ],
    license='Apache License, Version 2.0',
    description='A Django app for consuming the WhenIWork REST API',
    long_description='README.md',
)
