from cveutils import CVE

def test():
    cve = CVE("CVE-2022-35405")
    assert cve.ID == "CVE-2022-35405"


if __name__ == "__main__":
    test()
    print("Everything passed")
