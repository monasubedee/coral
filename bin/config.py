from configparser import SafeConfigParser
import os
from flask_httpauth import HTTPBasicAuth

parser = SafeConfigParser(os.environ)
parser.read('config.ini')
api_host = parser.get('api', 'host')
host_name = parser.get('server', 'host_name')
port = parser.get('server', 'port')

kbauth = HTTPBasicAuth()
kbuser = {
    "knowledge": "bank"
}

@kbauth.get_password
def get_pw(username):
    if username in kbuser:
        return kbuser.get(username)
    return None
