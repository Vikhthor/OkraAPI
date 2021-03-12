# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in okra_pay/__init__.py
from okra_pay import __version__ as version

setup(
	name='okra_pay',
	version=version,
	description='A demo payment platform using Okra API',
	author='Victor Maduforo',
	author_email='victormaduforo@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
