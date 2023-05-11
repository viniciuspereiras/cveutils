import requests
from datetime import datetime

API_URL = "https://services.nvd.nist.gov/rest/json/cve/1.0/"

class CVSSDictionary(dict):
    """
    A dictionary that allows access to its keys as attributes
    """
    def __getattr__(self, key):
        return self[key]
    
    def __str__(self) -> str:
        return self.baseScore

class CVENotFound(Exception):
    pass

class CVE:
    """
    A class that represents a CVE

    :param CVEID: The CVE ID
    :type CVEID: str

    :ivar ID: The CVE ID
    :vartype ID: str
    
    :ivar info: The MITRE api response json
    :vartype info: dict

    :ivar description: The CVE description
    :vartype description: str

    :ivar cvss_v2: The CVSS v2 score
    :vartype cvss_v2: dict

    :ivar cvss_v3: The CVSS v3 score
    :vartype cvss_v3: dict

    :ivar published_date: The CVE published date
    :vartype published_date: str

    :ivar last_modified_date: The CVE last modified date
    :vartype last_modified_date: str

    :ivar assigner: The CVE assigner
    :vartype assigner: str

    :ivar references: The CVE references
    :vartype references: list

    :returns: A CVE object
    """
    def __init__(self, CVEID) -> None:
        self.ID = CVEID
        self.info = self.getCVEInfo()
        if 'message' in self.info.keys() and 'Unable to find vuln' in self.info['message']:
            raise CVENotFound('CVE not found')
        self.description = self.info["result"]["CVE_Items"][0]["cve"]["description"]["description_data"][0]["value"]
        self.getCVSS()
        self.published_date = self.publishedDate()
        self.last_modified_date = self.lastModifiedDate()
        self.assigner = self.info["result"]["CVE_Items"][0]["cve"]["CVE_data_meta"]["ASSIGNER"]
        self.references = self.info["result"]["CVE_Items"][0]["cve"]["references"]["reference_data"]

    def __str__(self) -> str:
        return self.ID

    def getCVEInfo(self):
        """
        Gets the MITRE api response json from a CVE ID
        """
        return requests.get(API_URL + self.ID).json()
    

    def _returnEmptyCVSSInfo(self):
        self.cvss_v2 = {}
        self.cvss_v3 = {}
        return None
       
    def getCVSS(self):
        """
        Gets the CVSS score and version from a CVE ID
        """
        output = {}
        try:
            json_response = self.info
            json_impacts = json_response['result']['CVE_Items'][0]['impact']
            if len(json_impacts) <= 0:
                return self._returnEmptyCVSSInfo()
        except:
            return self._returnEmptyCVSSInfo()
        if 'baseMetricV3' in json_impacts:            
            self.cvss_v3 = CVSSDictionary(json_impacts['baseMetricV3']['cvssV3'])
        elif 'baseMetricV2' in json_impacts:
            self.cvss_v2 = CVSSDictionary(json_impacts['baseMetricV2']['cvssV2'])
        return None

    def publishedDate(self):
        p = self.info["result"]["CVE_Items"][0]["publishedDate"]
        datetime_obj = datetime.fromisoformat(p[:-1])  # remove the 'Z' suffix and parse the string
        date_str = datetime_obj.date().isoformat()
        return date_str
    
    def lastModifiedDate(self):
        p = self.info["result"]["CVE_Items"][0]["lastModifiedDate"]
        datetime_obj = datetime.fromisoformat(p[:-1])
        date_str = datetime_obj.date().isoformat()
        return date_str
    

if '__main__' == __name__:
    cve = CVE("CVE-2022-35405")

    print(cve.ID)
