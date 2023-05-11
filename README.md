# cveutils
![logo](https://raw.githubusercontent.com/viniciuspereiras/cveutils/main/static/logo.png)

[![PyPI](https://img.shields.io/pypi/v/cveutils?style=flat)](https://pypi.python.org/pypi/cveutils/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)

This library provides functionality for fetching and parsing information about Common Vulnerabilities and Exposures (CVE) using the NIST National Vulnerability Database (NVD) RESTful API.
## Instalation
```bash
pip install cveutils
```
## Usage
To use this library, simply import the CVE class and initialize an instance with a CVE ID as a string.

```python

from cveutils import CVE

cve = CVE('CVE-2021-12345')
```
### CVE Object

The `CVE` object has the following attributes:
- `ID`: The CVE ID
- `info`: The full JSON response from the NVD API for the given CVE ID
- `description`: The description of the CVE
- `cvss_v2`: A dictionary containing the CVSSv2 score and related metrics (if available)
- `cvss_v3`: A dictionary containing the CVSSv3 score and related metrics (if available)
- `published_date`: The published date of the CVE in ISO format (YYYY-MM-DD)
- `last_modified_date`: The last modified date of the CVE in ISO format (YYYY-MM-DD)
- `assigner`: The organization that assigned the CVE ID
- `references`: A list of references related to the CVE

The `cvss_v2` and `cvss_v3` attributes are instances of the CVSSDictionary class, which allows access to the dictionary keys as attributes.
# Example Usage

```python

from cveutils import CVE

cve = CVE('CVE-2021-12345')

print(cve.ID)
print(cve.description)
print(cve.cvss_v3.baseScore)
print(cve.published_date)
print(cve.last_modified_date)
print(cve.assigner)
print(cve.references)
```
Output:
```css

CVE-2021-12345
Description of the vulnerability
7.8
2021-01-01
2021-02-01
MITRE
['https://example.com/reference1', 'https://example.com/reference2']

```
