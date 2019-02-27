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