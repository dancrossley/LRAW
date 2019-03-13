from lraw import lraw
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #Disable certificate validation warnings
lr = lraw('<LR IP>', '<API Bearer Token>')
lr.list_hosts()
lr.create_case()