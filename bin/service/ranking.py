import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"

def getRankingList(criteria, userId):
    req = urllib.request.Request(
        (api_host + "/stats/ranking/list?criteria="+criteria+"&userId="+userId), method="GET") # criteria 0 for ranking page.
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def getRankingInfo(userId):
    req = urllib.request.Request(
        (api_host + "/stats/getRankingListInfo?userId="+userId), method="GET")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def getRankingByUserId(userId):
    req = urllib.request.Request(
        (api_host + "/stats/getRankingbyuserID?userId="+str(userId)), method="GET") # criteria 0 for ranking page.
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def getRankingManabuList(data):
    json_data = json.dumps(data).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/stats/ranking/manabuList"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        res = json.loads(response_body)
    return res

def getRankingCommentList(data):
    json_data = json.dumps(data).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/stats/ranking/commentList"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        res = json.loads(response_body)
    return res

def getRankingTameruList(data):
    json_data = json.dumps(data).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/stats/ranking/tameruList"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        res = json.loads(response_body)
    return res
