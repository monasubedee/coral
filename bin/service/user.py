import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"


# def getAvatorImage(userId):
#     url = config.api_host + "/user/picture?userId=" + str(userId)
#     method = "GET"
#     req = urllib.request.Request(url, method=method)
#     with urllib.request.urlopen(req) as res:
#         response_body = res.read().decode("utf-8")
#         result = json.loads(response_body)
#         if result['result'] == 'ng':
#             avatorImage = '/static/img/mypage_icon.png'
#         else:
#             avatorImage = result['data']['pictureImage']
#
#     return avatorImage


def postUserPicture(userId, pictureImage):
    url = api_host + "/user/picture"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(
        {"userId": userId, "pictureImage": pictureImage}).encode("utf-8")

    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)


def fetchUserProfile(userId):
    url = api_host + "/user/profile?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        result = json.loads(response_body)
    return result

def fetchUserProfileForContact(userId):
    url = api_host + "/user/profileContact?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        result = json.loads(response_body)
    return result

def requestPasswordReset(mail):
    url = api_host + "/auth/password/reset"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"mail": mail}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)


def definePassword(userpass, token):
    # API access as wrapper
    url = api_host + "/auth/password/set"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"password": userpass, "token": token}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        result = json.loads(response_body)
    return result
    # todo result or error object


def fetchFavedQuestions(userId):
    url = api_host + "/user/favedQuestions?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchAnswerdQuestions(userId):
    url = api_host + "/user/answeredQuestions?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchCreatedQuestions(userId):
    # api access 4
    url = api_host + "/user/createdQuestions?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def signup(email, password, userName,token):
    url = api_host + "/auth/signup"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"username": email, "password": password, "displayName": userName,"token":token}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        result = json.loads(response_body)
    return result

def fetchUserInfo(userId):
    # api access 4
    url = api_host + "/user/getInfo?userId=" + str(userId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)
