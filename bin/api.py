from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
import datetime
from service import question, user
import traceback

app = Blueprint("api", __name__, url_prefix="/api")
@app.route("/comment", methods=['POST'])
@login_required
def api_comment():
    userId = current_user.id

    # FIXME
    data = request.json
    questionId = data['questionId']
    comment = data['comment']

    result = question.postFeed(userId, questionId, comment)
    # todo handling error and define error response
    res = {
        "create": True,
        "result": "ok",
        "message": "question has been commented.",
    }

    return jsonify(res)


@app.route("/clip", methods=['POST'])
@login_required
def api_clip():
    userId = current_user.id

    # FIXME
    data = request.json
    questionId = data['questionId']

    # API access as wrapper
    result = question.postFav(userId, questionId)
    # todo handling error and define error response
    # response JSON
    res = {
        "create": True,
        "result": "ok",
        "message": "question has been clipped.",
    }

    return jsonify(res)


@app.route("/create", methods=['POST'])
@login_required
def api_create():

    # answersの形状がよろしくない．．
    variables = dict()
    variables["userId"] = current_user.id
    variables["categoryId"] = int(request.form["categoryId"])
    variables["sub_categoryId"] = int(request.form["sub_categoryId"])
    variables["questionText"] = request.form["questionText"]
    variables["questionType"] = int(request.form["questionType"])
    variables["descriptionText"] = request.form["descriptionText"]
    variables["draftFlag"] = request.form["draftFlag"]

    # questionPicture
    # <---- when questionPicture image was not uploaded.
    if request.form["questionPicture"] == '':
        variables["questionPictureId"] = 0
    # <---------------------------------------- when questionPicture image was uploaded.
    else:
        result = question.postPictureImage(
            current_user.id, request.form["questionPicture"])
        questionPictureId = result['data']['pictureId']
        variables["questionPictureId"] = int(questionPictureId)

    # descriptionPicture
    # <---- when descriptionPicture image was not uploaded.
    if request.form["descriptionPicture"] == '':
        variables["descriptionPictureId"] = 0
    # <---------------------------------------- when descriptionPicture image was uploaded.
    else:
        result = question.postPictureImage(
            current_user.id, request.form["descriptionPicture"])

        descriptionPictureId = result['data']['pictureId']
        # set qestionPictureId
        variables["descriptionPictureId"] = int(descriptionPictureId)

    variables["topicLabels"] = list()
    tmp_topicLabels = request.form.getlist("topicLabels[]")
    for entry in tmp_topicLabels:
        variables["topicLabels"].append(entry)

    variables["answers"] = list()
    idx = 0
    while True:
        tmp_correctFlag = request.form.get(
            "answers[" + str(idx) + "][correctFlag]")
        if tmp_correctFlag == None:
            break
        else:
            tmp_label = request.form.get(
                "answers[" + str(idx) + "][label]")
            variables["answers"].append(
                {"correctFlag": tmp_correctFlag, "label": tmp_label})
            idx += 1

    try:
        obj = {
            "userId": variables["userId"],
            "categoryId": variables["categoryId"],
            "sub_categoryId": variables["sub_categoryId"],
            "questionText": variables["questionText"],
            "questionType": variables["questionType"],
            "questionPictureId": variables["questionPictureId"],
            "descriptionText": variables["descriptionText"],
            "descriptionPictureId": variables["descriptionPictureId"],
            "topicLabels": variables["topicLabels"],
            "answers": variables["answers"],
            "draftFlag": variables["draftFlag"],
        }
        result = question.postQuestion(obj)
        res = {
            "create": True,
            "result": "ok",
            "message": "question has been created.",
        }
    except:
        res = {
            "create": False,
            "result": "ng",
            "message": "question has been created.",
        }

    return jsonify(res)


# 問題編集
@app.route("/question/edit", methods=['POST'])
@login_required
def api_question_edit():

    # FIXME: create.js - "type: 'POST',"を追加すること．
    # answersの形状がよろしくない．．
    # received request POST
    variables = dict()
    variables["userId"] = current_user.id
    variables["categoryId"] = int(request.form["categoryId"])
    variables["sub_categoryId"] = int(request.form["sub_categoryId"])
    variables["questionText"] = request.form["questionText"]
    variables["questionType"] = int(request.form["questionType"])
    variables["descriptionText"] = request.form["descriptionText"]
    variables["draftFlag"] = request.form["draftFlag"]
    variables["questionId"] = request.form["questionId"]

    # questionPicture
    # <---- when questionPicture image was not uploaded.
    if request.form["questionPicture"] == '':
        variables["questionPictureId"] = 0
    # <---------------------------------------- when questionPicture image was uploaded.
    else:
        result = question.postPictureImage(
            current_user.id, request.form["questionPicture"])
        questionPictureId = result['data']['pictureId']
        variables["questionPictureId"] = int(questionPictureId)

    # descriptionPicture
    # <---- when descriptionPicture image was not uploaded.
    if request.form["descriptionPicture"] == '':
        variables["descriptionPictureId"] = 0
    # <---------------------------------------- when descriptionPicture image was uploaded.
    else:
        result = question.postPictureImage(
            current_user.id, request.form["descriptionPicture"])

        descriptionPictureId = result['data']['pictureId']
        # set qestionPictureId
        variables["descriptionPictureId"] = int(descriptionPictureId)

    variables["topicLabels"] = list()
    tmp_topicLabels = request.form.getlist("topicLabels[]")
    for entry in tmp_topicLabels:
        variables["topicLabels"].append(entry)

    variables["answers"] = list()
    idx = 0
    while True:
        tmp_correctFlag = request.form.get(
            "answers[" + str(idx) + "][correctFlag]")
        if tmp_correctFlag == None:
            break
        else:
            tmp_label = request.form.get(
                "answers[" + str(idx) + "][label]")
            variables["answers"].append(
                {"correctFlag": tmp_correctFlag, "label": tmp_label})
            idx += 1

    try:

        obj = {
            "userId": variables["userId"],
            "categoryId": variables["categoryId"],
            "sub_categoryId": variables["sub_categoryId"],
            "questionText": variables["questionText"],
            "questionType": variables["questionType"],
            "questionPictureId": variables["questionPictureId"],
            "descriptionText": variables["descriptionText"],
            "descriptionPictureId": variables["descriptionPictureId"],
            "topicLabels": variables["topicLabels"],
            "answers": variables["answers"],
            "draftFlag": variables["draftFlag"],
            "questionId": variables["questionId"],
        }
        question.editQuestion(obj)

        print("success111")
        res = {
            "create": True,
            "result": "ok",
            "message": "question has been created.",
        }

    except Exception as e:
        print(traceback.format_tb(e.__traceback__))

        print("failed111")
        res = {
            "create": False,
            "result": "ng",
            "message": "question has been created.",
        }

    return jsonify(res)


@app.route("/fav", methods=['POST'])
@login_required
def api_fav():
    print(request.method)
    userId = current_user.id

    # FIXME
    data = request.json
    questionId = data['questionId']

    # API access as wrapper
    result = question.postFav(userId, questionId)
    return jsonify(result)


@app.route("/unfav", methods=['POST'])
@login_required
def api_unfav():
    userId = current_user.id
    data = request.json
    questionId = data['questionId']

    result = question.postUnFav(userId, questionId)
    # todo handling error and define error response
    res = {
        "create": True,
        "message": "question has been faved.",
        "result": "ok"
    }

    return jsonify(res)


@app.route("/profile_edit", methods=['POST'])
@login_required
def api_profile_edit():
    userId = current_user.id
    languageSet = request.form.getlist("languageSet[]")
    roles = request.form.getlist("roles[]")
    skillSet = request.form.getlist("skillSet[]")
    goal = request.form["goal"]
    pictureImage = request.form["profilePicture"]

    birthDate = datetime.date(int(request.form["birthYear"]), int(
        request.form["birthMonth"]), int(request.form["birthDay"])).strftime("%Y-%m-%d")
    hireDate = datetime.date(int(request.form["hireYear"]), int(
        request.form["hireMonth"]), int(request.form["hireDay"])).strftime("%Y-%m-%d")

    obj = {
        "userId": userId,
        "countryId": request.form["countryId"],
        "hireDate": hireDate,
        "birthDate": birthDate,
        "displayName": str(request.form["displayName"]),
        "gender": int(request.form["gender"]),
        "occupationId": int(request.form["occupationId"]),
        "goal": goal,
        "languageSet": languageSet,
        "roles": roles,
        "skillSet": skillSet
    }

    result = user.editUserProfile(obj)

    if(result["result"] == "ng"):
        return jsonify(result), 400
    if (pictureImage != ""):
        result = user.postUserPicture(result["userId"], pictureImage)

    return jsonify(result)
