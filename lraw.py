import requests
import logging
import urllib3

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
        print(self.response.text)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #Disable certificate validation warnings

lr = lraw('192.168.38.128', 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOi0xMDAsImp0aSI6IjcxOTFhZWYwLWVlN2EtNDJmZC1iZmIwLWZhZmM1Y2I4ZTZiMyIsImNpZCI6IjBEQjVDMjA5LUQ0RDYtNDBGQS1CQzA3LTgwRDE1NEFDNzY5NyIsImlzcyI6ImxyLWF1dGgiLCJyaWQiOiJnbG9iYWxBZG1pbiIsInBpZCI6LTEwMCwic3ViIjoiTG9nUmh5dGhtQWRtaW4iLCJleHAiOjE1ODI3ODM1MDYsImRlaWQiOjEsImlhdCI6MTU1MTI0NzUwNn0.nM6wd2cD9RluQx0-STBPIjYqmQOHkS5pgaT4tw7l9gu06BGPpGvNTRU6Lx-5vZimIyQLMZW0V62OKVJ1u0b1u80R3cYx8QTRZLQw15cSr-2a9d4rGyAA58abo5xz9dsas1ihIzZ6_DsUPRBIz7NgS71-VBljX-QUxKPUKQSycJMXUr2clA2nWDRmhQJm0dtUM_gg9Au8XjPHdp3A8Z6J7htSANBS9oloI6NDS_DrP8WLkLDzaA1E3GMy2UWxMOuLKV3qy6l3UNzpm5obSIqkTGtvmrTdhcJeTkWc5_1kcyYUt7QqUiD9XijryUE3je5IHCOnjLhT58vOCpcOecSEIA')
lr.list_hosts()