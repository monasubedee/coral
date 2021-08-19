import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"


def fetchUserStats(userId):
    url = api_host + "/stats/user?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchRecordCount(userId):
    url = api_host + "/stats/record_count?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def questioncount():
    url = api_host + "/question/count"
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def fetchGraphRecord(userId):
    url = api_host + "/stats/graph_record?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def getRecordCount(userId):
    req = urllib.request.Request(
        (api_host + "/stats/record_count?userId=" + str(userId)), method="GET")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def fetchChallenge(userId):
    url = api_host + "/stats/challenge?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchActivity(userId):
    url = api_host + "/stats/activity?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchRankingByUserId(userId):
    url = api_host + "/stats/getRankingbyuserID?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchRankingComments(userId):
    url = api_host + "/stats/ranking/comments?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchRankingAccumulated(userId):
    url = api_host + "/stats/ranking/accumulated?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchRankingLearn(userId):
    url = api_host + "/stats/ranking/learn?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)
