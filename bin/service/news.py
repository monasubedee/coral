import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"

def getNews(userId,isHomePage):
    req = urllib.request.Request(
        (api_host + "/news/get?userId=" + str(userId) + "&isHomePage="+str(isHomePage)), method="GET")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def getNewsDetail(newsId,userId):
    req = urllib.request.Request(
        (api_host + "/news/detail?id=" + str(newsId))+"&userId="+str(userId), method="GET")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def registerNews(userId, title, description, isPublished):
    # API access as wrapper
    # print(userId,title,description,isPublished)
    url = api_host + "/news/hogehoge/register"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"userId": userId, "title": title, "description" : description, "isPublished" : isPublished}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        result = json.loads(response_body)
    return result

def editNews(userId, title, description, isPublished, noticeId):
    # API access as wrapper
    url = api_host + "/news/hogehoge/edit"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"userId": userId, "title": title, "description" : description, "isPublished" : isPublished, "noticeId" : noticeId}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        result = json.loads(response_body)
    return result

def findId(noticeId):
    url = api_host + "/news/findbyId?id="+str(noticeId)
    method = "GET"
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def deleteNews(id):
    # API access as wrapper
    url = api_host + "/news/hogehoge/edit"
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

def news_list_delete(data):
    obj = data
    json_data = json.dumps(obj).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/news/hogehoge/delete"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        # print("response_body----->",response_body)
        res = json.loads(response_body)
    return res
