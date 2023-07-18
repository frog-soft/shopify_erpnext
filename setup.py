from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in shopify_erpnext/__init__.py
from shopify_erpnext import __version__ as version

setup(
	name="shopify_erpnext",
	version=version,
	description="shopify connector for erpnext",
	author="json_wang",
	author_email="sonic3k@qq.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
