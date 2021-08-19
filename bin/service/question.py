import config
import urllib.request
import json
import urllib.error
import requests

api_host = config.api_host+"/api/v1"

def postQuestion(question):
    url = api_host + "/question/create"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(question).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)


def editQuestion(question):
    url = api_host + "/question/edit"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(question).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)


def fetchRefineSearch(userId):
    obj = {
        "userId": userId
    }
    json_data = json.dumps(obj).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/question/refinesearch"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchSortRefineSearch(data):
    json_data = json.dumps(data).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/question/refinesearch"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        res = json.loads(response_body)
    return res

def fetchRefineSearchByQuestion(data):
    json_data = json.dumps(data).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/question/refinesearchByQuestionId"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        res = json.loads(response_body)
    return res


def fetchQuestionByUserId(userId, resolveManabuFlag):
    url = api_host + "/question/get?userId="+str(userId)+"&resolveManabuFlag="+str(resolveManabuFlag)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    try:
        with urllib.request.urlopen(req) as res:
            response_body = res.read().decode("utf-8")

            result = json.loads(response_body)
            if result['result']=='ng':
                return {'questionData': None, 'next_day': result['data'],'newWeekFlag' : result['newWeekFlag']}

            questionData = {
                'questionText': result['data']['questionText'],
                'questionType': result['data']['questionType'],
                'correctRate': 0,
                'questionId': result['data']['questionId'],
                'questionPictureURL': result['data']['questionPicture'],
                'topicLabel' : result['data']['topicLabels']
            }
            answerData = list()
            if result['data']['questionType'] == 6:
                for entry in result['data']['answers']:
                    answerData.append(
                        {
                            'answerId': entry['answerId'],
                            'answer': entry['answer'],
                            'strType' : entry['strType']
                        }
                    )
            else:
                for entry in result['data']['answers']:
                    answerData.append(
                        {
                            'answerId': entry['id'],
                            'label': entry['label'],
                        }
                    )
    except urllib.error.HTTPError:
        return urllib.error.HTTPError
    return {'questionData': questionData, 'answerData': answerData, 'newWeekFlag' : result['newWeekFlag']}


def fetchQuestionByQuestionId(questionId):
    url = api_host + "/question/get?questionId=" + str(questionId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchCorrectRate(questionId):
    url = api_host + "/question/correctRate?questionId=" + str(questionId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        result = json.loads(response_body)
    return result['data']['correctRate']


def fetchPictureImage(pictureId):
    url = api_host + "/question/picture?pictureId=" + str(pictureId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        result = json.loads(response_body)
    returnValue='ng'
    if result['result']!='ng':
        returnValue=result['data']['pictureImage']
    return returnValue


def fetchPictureImages(pictureIds):
    url = api_host + "/question/pictures?pictureId=" + str(pictureIds)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def postPictureImage(userId, pictureImage):
    url = api_host + "/question/picture"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"userId": userId, "pictureImage": pictureImage}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)


def fetchCategory():
    url = api_host + "/question/category"
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchQuestionType():
    url = api_host + "/question/type"
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def postAnswer(data):
    url = api_host + "/question/answer"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    # obj = {"userId": userId, "questionId": questionId,
    #        "answers": answers, "elapsedTime": elapsedTime}
    json_data = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        result = json.loads(response_body)
    return result


def postFeed(userId, questionId, comment):
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


def postFav(userId, questionId):
    url = api_host + "/question/fav"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"userId": userId, "questionId": questionId}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)


def postUnFav(userId, questionId):
    url = api_host + "/question/unfav"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"userId": userId, "questionId": questionId}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)


def postQuesRate(userId, questionId,rating):
    url = api_host + "/question/rate"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"userId": userId, "questionId": questionId,"rating":rating}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)

def question_create_csv(userId, csvFile):
    url = api_host + "/question/questionCreateCSV"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    obj = {"userId": userId, "file": csvFile.decode("utf-8")}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)

def delete(obj):
    # API access as wrapper
    url = api_host + "/question/delete"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    # obj = {"id": id}
    json_data = json.dumps(obj).encode("utf-8")
    req = urllib.request.Request(
        url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        result = json.loads(response_body)
    return result

def favQuestionByUserId(data):
    json_data = json.dumps(data).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/question/favQuestionListByUserId"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        res = json.loads(response_body)
    return res

def getCommentData(questionId):
    url = api_host + "/question/getCommentData?questionId="+str(questionId)
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def fetchCSVFileList():
    url = api_host + "/question/getQuestionCSV"
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

def deleteCSVFileList(id):
    # API access as wrapper
    url = api_host + "/question/deleteQuestionCSV"
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
