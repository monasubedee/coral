from flask import Blueprint, render_template, request, jsonify, abort, url_for, redirect
from flask_login import login_required, current_user
from service import user, question, tag, company, setting
import json
import base64
import config

app = Blueprint("question", __name__, url_prefix="/question")


# 問題詳細
@app.route("/detail/<question_detail_id>", methods=["GET", "POST"])
def question_detail(question_detail_id):
    if current_user.is_authenticated:

        userId = current_user.id

        result = question.fetchQuestionByQuestionId(question_detail_id)

        data = {
            'categoryId': result['data']['categoryId'],
            'descriptionPictureId': result['data']['descriptionPictureId'],
            'descriptionText': result['data']['descriptionText'],
            'questionPictureId': result['data']['questionPictureId'],
            'questionText': result['data']['questionText'],
            'questionType': result['data']['questionType'],
            'sub_categoryId': result['data']['sub_categoryId'],
            'topicLabels': result['data']['topicLabels'],
            'questionId': result['data']['questionId']
        }

        answerData = list()
        for entry in result['data']['answers']:
            answerData.append(
                {'answerId': entry['answerId'], 'correctFlag': entry['correctFlag'], 'id': entry['id'], 'label': entry['label']})

        # カテゴリーを取る
        result = question.fetchCategory()

        categoryData = list()
        subcategoryData = list()

        for entry in result['category']:
            categoryData.append({
                'id': entry['id'],
                'label': entry['label']
            })
        for entry in result['occupation']:
            subcategoryData.append({
                'id': entry['id'],
                'label': entry['label']
            })

        # 画像を取る
        if data['descriptionPictureId'] != '0' and data['questionPictureId'] == '0':
            picId = data['descriptionPictureId']
        elif data['descriptionPictureId'] == '0' and data['questionPictureId'] != '0':
            picId = data['questionPictureId']
        elif data['descriptionPictureId'] != '0' and data['questionPictureId'] != '0':
            picId = str(data['descriptionPictureId']) + \
                "," + str(data['questionPictureId'])
        else:
            picId = 0

            result = question.fetchPictureImages(picId)

            pictureData = result['data']

        # 問題タイプ

            questionType = list()

            for entry in result['questionType']:
                questionType.append({
                    'id': entry['id'],
                    'label': entry['label']
                })

        # when create was tapped on home by user
        if request.method == "GET":
            # API ACCESS 1
            userId = current_user.id
            #avatorImage = user.getAvatorImage(userId)

            # FIXME: category and subcategory with API ACCESS 2

            return render_template('question_detail.html',
                                   #avatorImage=avatorImage,
                                   data=data,
                                   categoryData=categoryData, subcategoryData=subcategoryData, answerData=answerData, questionType=questionType, pictureData=pictureData)

        # when question creator was posted by user
        else:
            # FIXME: question_edit.js - "type: 'POST',"を追加すること．
            # received request POST
            userId = current_user.id
            categoryId = request.form["categoryId"]
            sub_categoryId = request.form["sub_categoryId"]
            questionText = request.form["questionText"]
            questionType = request.form["questionType"]

            # API access as wrapper

            # response JSON
            res = {
                "create": True,
                "result": "ok",
                "message": "question has been created.",
            }

            return jsonify(res)
    else:
        return redirect(url_for('index'))

# 問題編集完了
@app.route("/question/edit/complete", methods=["GET"])
def question_edit_complete():
    if current_user.is_authenticated:

        # API ACCESS 1
        pageTitle = 'edit'

        try:
            userId = current_user.id
            #avatorImage = user.getAvatorImage(userId)
            logined = 'true'
        except:
            userId = 0
            #avatorImage = ''
            logined = 'false'

        return render_template('question_edit_complete.html', title=pageTitle, logined=logined)

    else:
        return redirect(url_for('index'))

@app.route("/question/edit/<question_edit_id>", methods=["GET", "POST"])
def question_edit(question_edit_id):
    if current_user.is_authenticated:
        userId = current_user.id

        result = question.fetchQuestionByQuestionId(question_edit_id)

        data = {
            'categoryId': result['data']['categoryId'],
            'descriptionPictureId': result['data']['descriptionPictureId'],
            'descriptionText': result['data']['descriptionText'],
            'questionPictureId': result['data']['questionPictureId'],
            'questionText': result['data']['questionText'],
            'questionType': result['data']['questionType'],
            'sub_categoryId': result['data']['sub_categoryId'],
            'topicLabels': result['data']['topicLabels'],
            'questionId': result['data']['questionId']
        }

        answerData = list()
        for entry in result['data']['answers']:
            answerData.append(
                {'answerId': entry['answerId'], 'correctFlag': entry['correctFlag'], 'id': entry['id'], 'label': entry['label']})

        result = question.fetchCategory()

        categoryData = list()
        subcategoryData = list()

        for entry in result['category']:
            categoryData.append({'id': entry['id'], 'label': entry['label']})
        for entry in result['occupation']:
            subcategoryData.append(
                {'id': entry['id'], 'label': entry['label']})

        # 問題タイプ

        result = question.fetchQuestionType()

        questionType = list()

        for entry in result['questionType']:
            questionType.append({'id': entry['id'], 'label': entry['label']})

        # when create was tapped on home by user
        if request.method == "GET":
            # API ACCESS 1
            userId = current_user.id
            #avatorImage = user.getAvatorImage(userId)

            # FIXME: category and subcategory with API ACCESS 2

            return render_template('question_edit.html', data=data, categoryData=categoryData, subcategoryData=subcategoryData, answerData=answerData, questionType=questionType)

        # when question creator was posted by user
        else:
            # FIXME: question_edit.js - "type: 'POST',"を追加すること．
            # received request POST
            userId = current_user.id
            categoryId = request.form["categoryId"]
            sub_categoryId = request.form["sub_categoryId"]
            questionText = request.form["questionText"]
            questionType = request.form["questionType"]

            # API access as wrapper

            # response JSON
            res = {
                "create": True,
                "result": "ok",
                "message": "question has been created.",
            }

            return jsonify(res)
    else:
        return redirect(url_for('index'))

@app.route('/create', methods=["GET","POST"])
def question_create():
    if current_user.is_authenticated:
        if request.method == "GET":
            userId = current_user.id
            teamData = setting.fetchTeam(userId)
            positionData = setting.fetchPosition(userId)
            return render_template('ver3/tameru/create/index.html',team = teamData['data'], position = positionData['data'])
        else:
            try:
                received_data = request.data
                received_data = received_data.decode('utf-8')
                data = json.loads(received_data)
                data["userId"] = current_user.id
                msg = question.postQuestion(data)

            except:
                return abort(500)
            return json.dumps(msg)
    else:
        return redirect(url_for('index'))

@app.route('/edit', methods=["GET","POST"])
def question_createbyId():
    if current_user.is_authenticated:
        if request.method == "GET":
            userId = current_user.id
            teamData = setting.fetchTeam(userId)
            positionData = setting.fetchPosition(userId)
            #return render_template('ver2.1/tameru/tameru_create.html',team = teamData['data'], position = positionData['data'])
            return render_template('ver3/tameru/create/index.html',team = teamData['data'], position = positionData['data'])
        else:
            try:

                # try:
                #     userId = current_user.id
                #     avatorImage = user.getAvatorImage(userId)
                #     logined = 'true'
                # except:
                    # userId = 1
                    # avatorImage = ''
                    # logined = 'false'
                received_data = request.data
                received_data = received_data.decode('utf-8')
                data = json.loads(received_data)
                data["userId"] = current_user.id

                #msg = company.CompanyInformationRegister(companyname,postalno,residence,street,cityname,fulladd,building,phoneno,companyurl,respname,respmail,respposition,billingname,b_postalno,b_residence,b_street,b_cityname,b_fulladd,b_building,userId)
                msg = question.editQuestion(data)

            except:
                return abort(500)
            return json.dumps(msg)
    else:
        return redirect(url_for('index'))

@app.route("/tameruList", methods=["POST"])
def tameru_list():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        data['userId'] = current_user.id
        result = question.fetchSortRefineSearch(data)
        return jsonify(result)
    else:
        return redirect(url_for('index'))

@app.route("/tameruByQuestionId", methods=["POST"])
def tameru_edit():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        result = question.fetchRefineSearchByQuestion(data)

        return jsonify(result)
    else:
        return redirect(url_for('index'))

@app.route("/", methods=["GET"])
#@config.kbauth.login_required
def tameru_template():
    if current_user.is_authenticated:
        userId = current_user.id
        # retrieve tag, company_team, company_position
        tagResult = tag.fetchTag(userId)

        company_team = setting.fetchTeam(userId)

        company_positions = setting.fetchPosition(userId)

        tameru_data = question.fetchRefineSearch(userId)

        return render_template('ver2.1/tameru/tameru.html', tag=tagResult, company_positions=company_positions, company_team=company_team)
    else:
        return redirect(url_for('index'))

@app.route("/questionCSV", methods=["POST"])
def createWithCSV():
    if current_user.is_authenticated:
        userId = current_user.id
        csvFile = request.files['file']
        csv_string = base64.b64encode(csvFile.read())
        result = question.question_create_csv(userId, csv_string)
        print('result',result)
        return json.dumps(result)
    else:
        return redirect(url_for('index'))

@app.route("/favQuestionList", methods=["POST"])
def favQuestionListByUserId():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        data['userId'] = current_user.id
        result = question.favQuestionByUserId(data)
        return json.dumps(result)
    else:
        return redirect(url_for('index'))

@app.route("/delete", methods=["POST"])
def delete_question():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        data['userId'] = int(current_user.id)
        result = question.delete(data)
        return jsonify(result)
    else:
        return redirect(url_for('index'))

@app.route("/getCommentData", methods=["GET"])
def getCommentData():
    questionId  = request.args.get("questionId",0)
    result = question.getCommentData(int(questionId))
    return jsonify(result)
    # if current_user.is_authenticated:
    #     questionId  = request.args.get("questionId",0)
    #     result = question.getCommentData(int(questionId))
    #     return jsonify(result)
    # else:
    #     return redirect(url_for('index'))
