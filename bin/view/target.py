from flask import Blueprint, render_template, request, redirect, url_for,abort,jsonify,json
from flask_login import current_user,login_required
from service import target, profile, stats
import json
import config
import datetime

app = Blueprint('target', __name__, url_prefix='/target')

@app.route("/", methods=["GET"])
# @config.kbauth.login_required
def target_index():
    if current_user.is_authenticated:
        userId = current_user.id
        data = target.fetchTargetText(userId)
        targetText = []
        idData = []
        meTargetVal = []
        meRatingDetail = []
        evaluateId = []
        for txt in data.get("data"):
            targetText.append(txt.get("targetText").replace("\n","<br />\n"))
            idData.append(txt.get("id"))
            meTargetVal.append(txt.get("ratingDetail").get("target"))
            meRatingDetail.append(txt.get("ratingDetail").get("topic"))
            evaluateId.append(txt.get("evaluateId"))
        targetTeam = target.fetchTeamTarget(userId)
        userProfile=profile.getUserProfile(userId)
        teamTargetText = targetTeam.get("data")
        return render_template('ver3/target/index.html', **locals())
    else:
        return redirect(url_for('index'))

@app.route("/self", methods=["GET"])
# @config.kbauth.login_required
def target_test():
    if current_user.is_authenticated:
        userId = current_user.id
        data = target.fetchTarget(userId)
        return jsonify(data)
    else:
        return redirect(url_for('index'))

@app.route("/others/<username>", methods=["GET"])
# @config.kbauth.login_required
def target_others(username):
    if current_user.is_authenticated:
        teamTargetText = target.fetchTeamTarget(current_user.id).get("data")
        for index, data in enumerate(teamTargetText):
            if data.get("displayName") == username:
                recordCount = stats.getRecordCount(data.get("userId"))["data"]
                meTargetText = teamTargetText[index]
                break
        print(meTargetText)
        print(recordCount)
        return render_template('ver3/target/others/index.html', **locals())
    else:
        return redirect(url_for('index'))

@app.route("/edit", methods=["GET"])
# @config.kbauth.login_required
def target_edit():
    if current_user.is_authenticated:
        teamTargetText = target.fetchTeamTarget(current_user.id).get("data")
        return render_template('ver3/target/edit/index.html', **locals())
    else:
        return redirect(url_for('index'))

@app.route("/", methods=["POST"])
# @config.kbauth.login_required
def register():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        data['userId'] = current_user.id

        #get current date
        current_date = datetime.date.today()
        #convert year week
        year, week_num, dayOfWeek = current_date.isocalendar()
        year_week = int(str(year) + str(week_num))

        data['yearWeek'] = year_week

        #in future, these topics word are get from user input targetText
        #currently, set as default
        topic_rating = { "WEBディレクション": 0, "ロジカルシンキング研修": 0, "営業の基礎" : 0, "挨拶": 0, "システムの基礎": 0}

        rating_detail = {
            "topic": topic_rating,
            "target": 0
        }

        data['ratingDetail'] = json.dumps(rating_detail)

        result = target.register(data)
        return json.dumps(result)
    else:
        return redirect(url_for('index'))

@app.route("/", methods=["DELETE"])
# @config.kbauth.login_required
def delete():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        result = target.delete(data)
        return json.dumps(result)
    else:
        return redirect(url_for('index'))

@app.route("/ratingDetail", methods=["PUT"])
# @config.kbauth.login_required
def update_ratingDetail():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        data['currentUserId']=str(current_user.id)
        data['ratingDetail'] = json.dumps(data['ratingDetail'])
        result = target.update_ratingDetail(data)
        return json.dumps(result)
    else:
        return redirect(url_for('index'))
