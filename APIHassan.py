import requests
import json
import jsonpath

url = "http://localhost:3000/api/collection"
header = {'Content-Type': 'application/json', 'X-Metabase-Session': 'a2bb2e95-c882-4a20-8e79-1981d83054b1'}


def test_GetDatabases():

    res = requests.get(url, headers=header)
    res_ = res.json()
    assert res_[0]["name"] == "Our analytics"


