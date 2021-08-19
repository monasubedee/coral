import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"

def getUserProfile(userId):
    req = urllib.request.Request(
        (api_host + "/user/profile?userId=" + str(userId)), method="GET")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def getRankingByUserId(userId):
    req = urllib.request.Request(
        (api_host + "/stats/getRankingbyuserID?userId=" + str(userId)), method="GET")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def editUserProfile(profile):
    url = api_host + "/user/profile"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(profile).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)

def getProfileRank(userId):
    req = urllib.request.Request(
        (api_host + "/stats/getProfileRank?userId=" + str(userId)), method="GET")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)
