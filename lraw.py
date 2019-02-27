import requests
import logging
import urllib3
import json

class lraw:
    def __init__(self, server, token):
        self._server = server
        self._token = token
        self._headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + token,
        'cache-control': "no-cache",
        }
    
    def list_hosts(self):
        self.payload = ""
        self.url = "https://" + self._server + ":8501/lr-admin-api/hosts/"
        self.response = requests.request("GET", self.url, data=self.payload, headers=self._headers, verify=False)
        hosts = json.loads(self.response.text)
        print(json.dumps(hosts, indent=4))

    def create_case(self):
        url = "https://" + self._server + ":8501/lr-case-api/cases/"
        print(url)
        payload = "{\n  \"externalId\": \"EXTERNAL-1235\",\n  \"name\": \"System Compromise\",\n  \"priority\": 1,\n  \"dueDate\": \"2019-02-27T06:56:21Z\",\n  \"summary\": \"Investigated a potential system compromise. More details at http://example.com/.\"\n}"
        print(payload)
        response = requests.request("POST", url, data=payload, headers=self._headers, verify=False)
        print('response requested!')
        cases = json.loads(response.text)
        print(json.dumps(cases, indent=4))