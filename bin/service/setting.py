import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"

def postLearningSettings(data):
    # obj = {
    #     "userId": userId,
    #     "learn_setting": data
    # }

    json_data = json.dumps(data).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/settings/learn"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        res = json.loads(response_body)
    return res

def fetchSettingNotification(data):
    # POST method.
    obj = data
    json_data = json.dumps(obj).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/settings/notification"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        res = json.loads(response_body)
    return res

def getSettingNotification(userId):
    # GET method.
    url=api_host + "/settings/notification?userId="+str(userId)
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def getNewsDetail(newsId):
    req = urllib.request.Request(
        (api_host + "/news/notice_delete_byId?id=" + str(newsId)), method="GET")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def registerOccupation(userId, occupationName):
    url = api_host + "/res/company_occupations/register"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(
        {"userId": userId, "occupationName": occupationName}).encode("utf-8")

    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)

def registerPosition(userId, positionName):
    url = api_host + "/res/company_positions/register"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(
        {"userId": userId, "positionname": positionName}).encode("utf-8")

    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)

def registerTeam(userId, teamName):
    url = api_host + "/res/company_teams/register"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(
        {"userId": userId, "teamname": teamName}).encode("utf-8")

    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)

def fetchTeam(userId):
    url = api_host + "/res/company_teams/get?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchPosition(userId):
    url = api_host + "/res/company_positions/get?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchOccupation(userId):
    url = api_host + "/res/company_occupations/get?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def postmemberinvite(data):
    obj = data
    json_data = json.dumps(obj).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/settings/member_add"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    res = json.loads(response_body)
    return res

def memberEdit(data):
    obj = data
    json_data = json.dumps(obj).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/settings/member_edit"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    res = json.loads(response_body)
    return res

def getMemberSelect(userId):
    url = api_host + "/settings/member_select?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def getmemberlist(userId):
    url = api_host + "/user/getMemberList?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def member_delete(data):

    obj = data
    json_data = json.dumps(obj).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/user/delete"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")

        res = json.loads(response_body)
    return res

def deletePosition(id):
    # API access as wrapper
    url = api_host + "/settings/positionDelete"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"id": id}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        result = json.loads(response_body)
    return result

def deleteTeam(id):
    # API access as wrapper
    url = api_host + "/settings/teamDelete"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"id": id}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        result = json.loads(response_body)
    return result

def fetchLearningSetting(userId):
    url = api_host + "/settings/get_LearningSetting?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def fetchKnowledgePack(userId):
    url = api_host + "/settings/knowledgePack?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def register_event(obj):
    json_data = json.dumps(obj).encode("utf-8")
    api_host=config.api_host+"/api/v2"
    url = api_host + "/event"
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        url, data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    res = json.loads(response_body)
    return res

def update_event(obj):
    json_data = json.dumps(obj).encode("utf-8")
    api_host=config.api_host+"/api/v2"
    url = api_host + "/event"
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        url, data=json_data, method="PUT", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    res = json.loads(response_body)
    return res

def get_eventlist(userId):
    api_host=config.api_host+"/api/v2"
    url = api_host + "/event?userId="+str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def delete_event(obj):
    api_host=config.api_host+"/api/v2"
    url=api_host + "/event"
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
