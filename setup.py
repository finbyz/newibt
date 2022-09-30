from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in newibt/__init__.py
from newibt import __version__ as version

setup(
	name="newibt",
	version=version,
	description="custom app",
	author="ibt",
	author_email="info@finbyz.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
