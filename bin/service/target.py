import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v2"

def fetchTargetText(userId):
    url=api_host + "/target?userId="+str(userId)
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req) as res:
            response_body = res.read().decode("utf-8")
    except urllib.error.HTTPError:
        return urllib.error.HTTPError
    return json.loads(response_body)

def fetchTeamTarget(userId):
    url=api_host + "/target/targetTeamUsers?userId="+str(userId)
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req) as res:
            response_body = res.read().decode("utf-8")
    except urllib.error.HTTPError:
        return urllib.error.HTTPError
    return json.loads(response_body)

def fetchTarget(userId):
    url=api_host + "/target?userId="+str(userId)+"&isLimit=False"
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req) as res:
            response_body = res.read().decode("utf-8")
    except urllib.error.HTTPError:
        return urllib.error.HTTPError
    return json.loads(response_body)

def delete(obj):
    url=api_host + "/target/"
    method = "DELETE"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req) as res:
            response_body = res.read().decode("utf-8")
    except urllib.error.HTTPError:
        return urllib.error.HTTPError
    return json.loads(response_body)

def register(obj):
    url=api_host + "/target/"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req) as res:
            response_body = res.read().decode("utf-8")
    except urllib.error.HTTPError:
        return urllib.error.HTTPError
    return json.loads(response_body)

def update_ratingDetail(obj):
    url=api_host + "/target/ratingDetail"
    method = "PUT"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req) as res:
            response_body = res.read().decode("utf-8")
    except urllib.error.HTTPError:
        return urllib.error.HTTPError
    return json.loads(response_body)
