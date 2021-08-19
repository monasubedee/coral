from flask import Blueprint, render_template, request, redirect, url_for,abort,jsonify,json
from flask_login import current_user,login_required
from service import user,setting, news, question
import json
import config

app = Blueprint('settings', __name__, url_prefix='/settings')

@app.route("/base", methods=["GET"])
# @config.kbauth.login_required
def settings_base():
    if current_user.is_authenticated:
        return render_template('ver2.1/settings/setting_base.html')
    else:
        return redirect(url_for('index'))

@app.route("/base/data", methods=["GET","POST"])
# @config.kbauth.login_required
def settings_base_data():
    if current_user.is_authenticated:
        if request.method == "GET":
            userId = current_user.id
            teamData = setting.fetchTeam(userId)
            positionData = setting.fetchPosition(userId)
            occupationData = setting.fetchOccupation(userId)
            status = request.args.get("status", "")
            obj={
                'team' : teamData['data'],
                'position' : positionData['data'],
                'occupation' : occupationData['data']
            }
            return json.dumps(obj)
            # //return render_template('ver2.1/settings/setting_base.html', methods=["GET", "POST"], status= status,team = teamData['data'], position = positionData['data'], occupation = occupationData['data'])
        else:
            userId = current_user.id
            data = request.get_json()
            res = setting.registerOccupation(userId,data.get('occupationName', [])) #data.get('positionname', []), data.get('teamname', []), data.get('occupationName', [])

            res1 = setting.registerPosition(userId, data.get('positionname', []))

            res2 = setting.registerTeam(userId, data.get('teamname', []))
            deletePositionList = data.get('delete_position_list', [])
            deleteTeamList = data.get('delete_team_list', [])
            if not deletePositionList == []:
                res3 = setting.deletePosition(deletePositionList)

            if not deleteTeamList == []:
                res4 = setting.deleteTeam(deleteTeamList)

            if (res["result"] == "ok") and (res1["result"] == "ok") and (res2["result"] == "0k"):
                return json.dumps(res)
                #return render_template('registration_thanks.html')
            else:
                return json.dumps(res)
                #return render_template('settings/base.html', methods=["GET", "POST"], message = "内容の保存に失敗しました")
    else:
        return redirect(url_for('index'))

# @app.route('/member', methods=['GET'])
# def base_member():
#     return redirect('settings/member.html')


@app.route('/learn', methods=["GET", "POST"])
# @config.kbauth.login_required
def base_learn():
    if current_user.is_authenticated:
        if request.method == "GET":
            status = request.args.get("status","")
            return render_template('ver2.1/settings/setting_learn.html',status=status)
        else :
            try:
                userId=current_user.id
                received_data = request.data

                received_data = received_data.decode('utf-8')
                data = json.loads(received_data)
                data['userId'] = userId

                msg = setting.postLearningSettings(data)

            except:
                return abort(500)

            return json.dumps(msg)
            # return redirect('settings/learn.html', message=msg,logined=logined)
    else:
        return redirect(url_for('index'))

@app.route('/mail', methods=["GET", "POST"])
# @config.kbauth.login_required
def setting_mail():
    if current_user.is_authenticated:
        pageTitle = 'ナレッジバンク設定'
        if request.method == 'GET':
            status = request.args.get("status","")
            return render_template('ver3/setting/mail/index.html',title=pageTitle, status=status)
        else:
            try:
                received_data = request.data

                received_data = received_data.decode('utf-8')
                data = json.loads(received_data)
                data['userId']=current_user.id
                msg = setting.fetchSettingNotification(data)
            except:
                return abort(500)

            return json.dumps(msg)
            # return redirect('/settings/mails.html', title=pageTitle, message=msg,logined=logined)
    else:
        return redirect(url_for('index'))

@app.route("/news_hoge", methods=["GET"])
# @config.kbauth.login_required
def news_list():
    if current_user.is_authenticated:
        try:
            userId = current_user.id
            #avatorImage = user.getAvatorImage(userId)
            logined = 'true'
        except:
            userId = current_user.id
            #avatorImage = ''
            logined = 'false'
        status = request.args.get("status", "")
        allNews=news.getNews(userId)
        return render_template("/settings/news.html", allNews=allNews,status=status)
    else:
        return redirect(url_for('index'))

@app.route("/news_deletebyId", methods=["GET"])
# @config.kbauth.login_required
def news_detail():
    if current_user.is_authenticated:
        newsId=int(request.args.get("id", 0))
        successMsg=setting.getNewsDetail(newsId)
        # return render_template("/settings/news.html", message=successMsg)
        return json.dumps(successMsg)
    else:
        return redirect(url_for('index'))

@app.route('/member_delete', methods=["POST", "GET"])
# @config.kbauth.login_required
def memberlistdelete():
    if current_user.is_authenticated:
        if request.method == "POST":
            try:
                received_data = request.data
                received_data = received_data.decode('utf-8')
                data = json.loads(received_data)
                msg = setting.member_delete(data)

            except:
                return abort(500)
            return json.dumps(msg)
    else:
        return redirect(url_for('index'))

@app.route('/member', methods=["GET","POST"])
# @config.kbauth.login_required
def member_invite():
    if current_user.is_authenticated:
        if request.method == "GET":
            userId = current_user.id
            memberdata = setting.getmemberlist(userId)
            status = request.args.get("status","")
            return render_template('ver2.1/settings/setting_member.html',memberlist = memberdata['data'],status=status )
        else:
            try:
                received_data = request.data
                received_data = received_data.decode('utf-8')
                data = json.loads(received_data)
                data['managerId']=current_user.id
                msg = setting.postmemberinvite(data)

            except:
                return abort(500)
            return json.dumps(msg)
    else:
        return redirect(url_for('index'))

@app.route('/member_edit', methods=["GET","POST"])
# @config.kbauth.login_required
def member_edit():
    if current_user.is_authenticated:
        if request.method == "POST":
            try:
                received_data = request.data
                received_data = received_data.decode('utf-8')
                data = json.loads(received_data)
                data['managerId']=current_user.id
                msg = setting.memberEdit(data)
            except:
                return abort(500)
            return json.dumps(msg)
    else:
        return redirect(url_for('index'))

@app.route("/member/list", methods=["GET"])
# @config.kbauth.login_required
def members_list():
    if current_user.is_authenticated:
        userId = current_user.id
        teamData = setting.fetchTeam(userId)
        positionData = setting.fetchPosition(userId)
        memberList = setting.getmemberlist(userId)
        data = {
            "memberList": memberList,
            "teamList" : teamData['data'],
            "positionList" : positionData['data']
        }
        return json.dumps(data)
    else:
        return redirect(url_for('index'))

@app.route("/get_LearningSetting", methods=["GET"])
# @config.kbauth.login_required
def get_learningsetting():
    if current_user.is_authenticated:
        userId = current_user.id
        data=setting.fetchLearningSetting(userId)

        return json.dumps(data)
    else:
        return redirect(url_for('index'))

@app.route("/import", methods=["GET"])
# @config.kbauth.login_required
def settings_import():
    if current_user.is_authenticated:
        print("enter is_authenticated")
        try:
            return render_template('ver3/setting/import/index.html')
        except:
            print("error")
    else:
        return redirect(url_for('index'))

@app.route("/notification", methods=["GET"])
# @config.kbauth.login_required
def getSettingNotification():
    if current_user.is_authenticated:
        userId = current_user.id
        result = setting.getSettingNotification(userId)
        return json.dumps(result)
    else:
        return redirect(url_for('index'))

@app.route("/get_CSVFileList", methods=["GET"])
# @config.kbauth.login_required
def get_csvfilelist():
    if current_user.is_authenticated:
        userId = current_user.id
        data = question.fetchCSVFileList()

        return json.dumps(data)
    else:
        return redirect(url_for('index'))

@app.route('/csvFileDelete', methods=["POST"])
# @config.kbauth.login_required
def csvfilelistdelete():
    if current_user.is_authenticated:
        try:
            received_data = request.data
            received_data = received_data.decode('utf-8')
            data = json.loads(received_data)
            msg = question.deleteCSVFileList(data['id'])

        except:
            return abort(500)
        return json.dumps(msg)
    else:
        return redirect(url_for('index'))

@app.route('/event', methods=["GET"])
def event():
    if current_user.is_authenticated:
        return render_template('ver3/setting/event/index.html')
    else:
        return redirect(url_for('index'))

@app.route("/knowledgePack", methods=["GET"])
#@config.kbauth.login_required
def knowledge_pack():
    try:
        userId = current_user.id
        data=setting.fetchKnowledgePack(userId)
        return json.dumps(data)
    except:
        return abort(500)


@app.route("/event", methods=["POST"])
#@config.kbauth.login_required
def register_event():
    try:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        data['userId'] = current_user.id
        result=setting.register_event(data)
        return json.dumps(result)
    except:
        return abort(500)

@app.route("/event", methods=["PUT"])
#@config.kbauth.login_required
def update_event():
    try:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        result=setting.update_event(data)
        return json.dumps(result)
    except:
        return abort(500)

@app.route("/event/list", methods=["GET"])
#@config.kbauth.login_required
def get_eventlist():
    try:
        userId = current_user.id
        data=setting.get_eventlist(userId)
        return json.dumps(data)
    except Exception as e:
        return abort(500)

@app.route("/event", methods=["DELETE"])
# @config.kbauth.login_required
def delete():
    if current_user.is_authenticated:
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        result = setting.delete_event(data)
        return json.dumps(result)
    else:
        return redirect(url_for('index'))
