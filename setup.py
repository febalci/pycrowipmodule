"""Crow/AAP Alarm Ip Module package."""
from setuptools import setup, find_packages

setup(
    name='pycrowipmodule',
    version='0.12',
    description='Library for Crow/AAP Alarm Ip Module',
    url='https://github.com/febalci/pycrowipmodule',
    maintainer='febalci',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    keywords='Crow/AAP Alarm Ip Module for Home Assistant',
    include_package_data=True,
    zip_safe=False
)

