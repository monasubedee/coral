from flask import Blueprint, render_template, request, jsonify, url_for, redirect
from flask_login import login_required, current_user
from service import profile, stats
from datetime import datetime
from time import strptime
import json
import config

app = Blueprint("profile", __name__, url_prefix="/profile")

@app.route("/", methods=["GET"])
# @config.kbauth.login_required
def fetch_profile():
    if current_user.is_authenticated:
        userId=current_user.id
        # print("userId = "+str(userId))
        userProfile=profile.getUserProfile(userId)
        record_count=stats.getRecordCount(userId)
        hiredate = userProfile["data"]["hireDate"].split("-")
        day = hiredate[2]
        month = hiredate[1]
        year = hiredate[0]
        return render_template('/ver2.1/pages/profile.html', userProfile=userProfile, record_count=record_count,day=day,month=month,year=year)
    else:
        return redirect(url_for('index'))

@app.route("/get", methods=["GET"])
def getProfileData():
    if current_user.is_authenticated:
        userId = current_user.id
        userProfile = profile.getUserProfile(userId)
        hiredate = userProfile["data"]["hireDate"].split("-")
        data={
            "userId":userId,
            "userProfile":userProfile,
            "record_count":stats.getRecordCount(userId),
            "hiredate" : hiredate,
            "day" : hiredate[2],
            "bday" :userProfile["data"]["birthDay"],
            "month"  : hiredate[1],
            "bmonth" : userProfile["data"]["birthMonth"],
            "year" : hiredate[0],
            "byear" : userProfile["data"]["birthYear"]
        }
        return json.dumps(data)
    else:
        return redirect(url_for('index'))

@app.route("/edit", methods=["POST"])
def edit_profile():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        data['userId'] = current_user.id
        msg = profile.editUserProfile(data)
        return json.dumps(msg)
    else:
        return redirect(url_for('index'))
