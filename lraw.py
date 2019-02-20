import requests
import logging

class LRAW:
    def __init__(self, server, token):
        self._server = server
        self._token = token
        self._headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + BEARER_TOKEN,
        'cache-control': "no-cache",
        }
    
    