import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"

def feed_question(userId, questionId, comment):
    url = api_host + "/question/feed"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"userId": userId, "questionId": questionId, "comment": comment}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)

def question_commentList(questionId, userId):
    url = api_host + "/question/comment/list?questionId="+str(questionId)+"&userId="+str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def deleteById(feedId):
    url = api_host + "/question/comment/delete"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"id": feedId}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)
