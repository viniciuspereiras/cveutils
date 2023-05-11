from setuptools import setup
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cveutils',
    version='0.6',
    description='This library provides functionality for fetching and parsing information about Common Vulnerabilities and Exposures (CVE) using the NIST National Vulnerability Database (NVD) RESTful API.',
    author='Vinicius Pereira (big0us)',
    author_email='vini@cius.xyz',
    package_dir={'': 'src'},
    packages=['cveutils'],
    install_requires=[
        'requests',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
