from flask import Blueprint, render_template, request, redirect,jsonify,json, url_for, redirect, session
from flask_login import login_required, current_user
from service import user, question, stats, profile, feed
from datetime import datetime
from time import strptime
import config

app = Blueprint("manabu", __name__, url_prefix="/manabu")

@app.route("/")
# @config.kbauth.login_required
def index():
    if current_user.is_authenticated:
        userId = current_user.id
        recordCount = stats.fetchRecordCount(userId)
        graphRecord = stats.fetchGraphRecord(userId)
        statsChallenge = stats.fetchChallenge(userId)
        userProfile=profile.getUserProfile(userId)
        hiredate = userProfile["data"]["hireDate"].split("-")
        day = hiredate[2]
        month = hiredate[1]
        year = hiredate[0]
        return render_template('ver2.1/manabu/manabu.html',userProfile=userProfile,day=day,month=month,year=year)
    else:
        return redirect(url_for('index'))

@app.route("/getGraphRecord")
def getGraphRecord():
    if current_user.is_authenticated:
        userId = current_user.id
        graphRecord = stats.fetchGraphRecord(userId)
        return json.dumps(graphRecord)
    else:
        return redirect(url_for('index'))

@app.route("/getChallenge")
def getChallenge():
    if current_user.is_authenticated:
        userId = current_user.id
        graphChallenge = stats.fetchChallenge(userId)
        return json.dumps(graphChallenge)
    else:
        return redirect(url_for('index'))

@app.route("/solve")
def solve():
    if current_user.is_authenticated:
        try:
            userId = current_user.id
            sessFlag = str(userId)
            completeFlag = request.args.get("completeFlag", 0)
            if int(completeFlag) == 1:
                session[sessFlag] = 1

            try:
                flag = session[sessFlag]
            except:
                session[sessFlag] = 0
                flag = 0

            result = question.fetchQuestionByUserId(userId, flag)

            if int(result['newWeekFlag']) == 1:
                session.pop(sessFlag, None)

            if result['questionData'] is None:
                return render_template(
                    'ver2.1/manabu/manabu_complete.html',
                    questionData=None,
                    answerData=None
                    )

            questionId = result['questionData']['questionId']
            result['questionData']['correctRate'] = question.fetchCorrectRate(
                questionId)

            return render_template(
                'ver3/manabu/solve/index.html',
                questionData=result['questionData'],
                answerData=result['answerData']
                )
        except:
            return render_template('404.html'), 404
    else:
        return redirect(url_for('index'))

@app.route("/result", methods=["POST"])
def result():
    if current_user.is_authenticated:
        received_data = request.data

        received_data = received_data.decode('utf-8')
        received = json.loads(received_data)
        received['userId']=current_user.id
        answerData = question.postAnswer(received)
        data = {
            'userId': received.get('userId'),
            'questionId': received.get('questionId'),
            'favState': answerData['data']['favState'],
            'ratingState': answerData['data']['ratingState'],
            'answerList': answerData['data']['answerList'],
            'correct': answerData['data']['correct'],
            'questionText': answerData['data']['questionText'],
            'descriptionText': answerData['data']['description'],
            "descriptionImage_url": answerData['data']['descriptionImage_url'],
            'challengeClear': answerData['data']['challengeClear']
        }

        correctAnswer = list()
        if received.get('questionType') == 6:
            correctAnswer.append(answerData['data']['correctAnswer'])
        else:
            for answer in answerData['data']['correctAnswer']:
                correctAnswer.append(answer['label'])

        correctRate = question.fetchCorrectRate(received.get('questionId'))
        data['correctRate'] = correctRate

        statsResult = stats.fetchUserStats(received.get('userId'))
        data["progressDailyChallengeRate"] = str(
            100 - statsResult['data']['countAnsweredToday'] / 5 * 100) if statsResult['data']['countAnsweredToday'] / 20 <= 1 else "0"
        data["countAnsweredToday"] = str(statsResult['data']['countAnsweredToday'])
        data["challengeRate"] = str(
            statsResult['data']['countAnsweredToday']) + "/5"
        data["progressDailyCorrectRate"] = str(
            100 - statsResult['data']['correctRatioToday'])
        data["dailyCorrectRate"] = str(
            statsResult['data']['correctRatioToday']) + "%"
        return json.dumps({
                        "data":data,
                        "correctAnswer":correctAnswer
                        })
    else:
        return redirect(url_for('index'))

@app.route("/favorite", methods=["POST"])
def manabu_fav():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        received = json.loads(received_data)
        received['userId']=current_user.id
        if received.get('fav')=='true':
            ques_fav = question.postFav(received.get('userId'),received.get('questionId'))
        else:
            ques_fav = question.postUnFav(received.get('userId'),received.get('questionId'))

        return json.dumps({
                    "ques_fav":ques_fav
                    })
    else:
        return redirect(url_for('index'))

@app.route("/rate", methods=["POST"])
def manabu_rate():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        received = json.loads(received_data)
        received['userId']=current_user.id
        if received.get('rating') !=None:
            ques_rate = question.postQuesRate(received.get('userId'),received.get('questionId'),received.get('rating'))
        else:
            ques_rate=''

        return json.dumps({
                    "ques_rate":ques_rate
                    })
    else:
        return redirect(url_for('index'))

@app.route("/comment", methods=["POST"])
def manabu_comment():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        received = json.loads(received_data)
        received['userId']=current_user.id
        if received.get('comment')!='':
            ques_comment = question.postFeed(received.get('userId'),received.get('questionId'),received.get('comment'))
        else:
            ques_comment =''

        return json.dumps({
                    "ques_comment":ques_comment
                    })
    else:
        return redirect(url_for('index'))

@app.route("/comment", methods=["DELETE"])
def manabu_uncomment():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        received = json.loads(received_data)
        id = received.get('id')
        if id !='':
            result = feed.deleteById(id)
        else:
            result =''

        return json.dumps({
                    "result" : result
                    })
    else:
        return redirect(url_for('index'))

@app.route("/complete", methods=["GET" ,"POST"])
def solve_complete():
    if current_user.is_authenticated:
        if request.method == 'GET':
            return render_template('ver2.1/manabu/manabu_complete.html')
        else:
            userId = current_user.id
            #avatorImage = user.getAvatorImage(userId)
            received_data = request.data
            received_data = received_data.decode('utf-8')
            received = json.loads(received_data)
            received['userId']=userId

            if received.get('fav')=='true':
                ques_fav = question.postFav(received.get('userId'),received.get('questionId'))
            else:
                ques_fav = question.postUnFav(received.get('userId'),received.get('questionId'))

            if received.get('rating') !=None:
                ques_rate = question.postQuesRate(received.get('userId'),received.get('questionId'),received.get('rating'))
            else:
                ques_rate=''
            if received.get('comment')!='':
                ques_comment = question.postFeed(received.get('userId'),received.get('questionId'),received.get('comment'))
            else:
                ques_comment =''

            return json.dumps({
                        #"avatorImage":avatorImage,
                        "ques_fav":ques_fav,
                        "ques_rate":ques_rate,
                        "ques_comment":ques_comment
                        })
    else:
        return redirect(url_for('index'))

@app.route("/getComment", methods=["GET"])
def getComment():
    if current_user.is_authenticated:
        userId = current_user.id
        questionId=int(request.args.get("id",0))
        commentList = feed.question_commentList(questionId, userId)
        return json.dumps(commentList)
    else:
        return redirect(url_for('index'))

@app.route("/unfav", methods=["POST"])
def unfavorite():
    if current_user.is_authenticated:
        received_data = request.data
        print("data is ", received_data)
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        userId = current_user.id
        result = question.postUnFav(userId,data.get('questionId'))
        return json.dumps(result)
    else:
        return redirect(url_for('index'))
