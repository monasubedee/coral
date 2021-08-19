import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"


def login(username, password):
    url = api_host + "/auth/login"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"username": username, "password": password}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)


def registration(profileData):
    url = api_host + "/auth/registration"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(profileData).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)

def checkInviteToken(token):
    url = api_host + "/settings/checkInviteToken"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(token).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)
