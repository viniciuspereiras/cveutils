from setuptools import setup, find_packages
import os

# ... other setup code ...

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='cveutils',
    version='0.3',
    description='This library provides functionality for fetching and parsing information about Common Vulnerabilities and Exposures (CVE) using the NIST National Vulnerability Database (NVD) RESTful API.',
    author='Vinicius Pereira (big0us)',
    author_email='vini@cius.xyz',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
