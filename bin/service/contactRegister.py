import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"

def saveContact(userId,inquiry_msg):
    url = api_host + "/contact/register"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(
        {"userId": userId, "inquiry_msg": inquiry_msg}).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)
