from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from service import ranking,profile,stats
from time import strptime
import json
import config

app = Blueprint("ranking", __name__, url_prefix="/ranking")

@app.route("/", methods=["GET"])
# @config.kbauth.login_required
def fetch_ranking():
    if current_user.is_authenticated:
        return render_template('ver2.1/pages/ranking.html')
    else:
        return redirect(url_for('index'))

@app.route("/list", methods=["GET"])
# @config.kbauth.login_required
def rankin_list():
    if current_user.is_authenticated:
        userId = current_user.id
        isHomePage=str(request.args.get("isHomePage", 0))
        rankingList = ranking.getRankingList(isHomePage, userId)
        return json.dumps(rankingList)
    else:
        return redirect(url_for('index'))

@app.route("/getRankingInfo", methods=["GET"])
# @config.kbauth.login_required
def rankin_Info():
    if current_user.is_authenticated:
        userId = current_user.id
        rankingInfo = ranking.getRankingInfo(userId)
        return json.dumps(rankingInfo)
    else:
        return redirect(url_for('index'))

@app.route("/getByUserId", methods=["GET"])
# @config.kbauth.login_required
def getRankingByUserId():
    if current_user.is_authenticated:
        userId = current_user.id
        rankingData = ranking.getRankingByUserId(userId)
        return json.dumps(rankingData)
    else:
        return redirect(url_for('index'))

@app.route("/manabuList", methods=["POST"])
# @config.kbauth.login_required
def manabuRankingList():
    if current_user.is_authenticated:
        received_data = request.data
        print("received data is",request.data)
        received_data = received_data.decode('utf-8')
        received = json.loads(received_data)
        received['userId']=current_user.id
        rankingList = ranking.getRankingManabuList(received)
        return json.dumps(rankingList)
    else:
        return redirect(url_for('index'))

@app.route("/commentList", methods=["POST"])
# @config.kbauth.login_required
def commentRankingList():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        received = json.loads(received_data)
        received['userId']=current_user.id
        rankingList = ranking.getRankingCommentList(received)
        return json.dumps(rankingList)
    else:
        return redirect(url_for('index'))

@app.route("/tameruList", methods=["POST"])
# @config.kbauth.login_required
def tameruRankingList():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        received = json.loads(received_data)
        received['userId']=current_user.id
        rankingList = ranking.getRankingTameruList(received)
        return json.dumps(rankingList)
    else:
        return redirect(url_for('index'))
