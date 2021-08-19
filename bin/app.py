# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, Markup, jsonify,abort, json
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
import datetime
import json
import config
from view import reset, manabu, contact, mypage, settings, profile, ranking, companys,\
                setting_news, news, question, policy, pageError, knowledge, introduction,\
                target, activities, event
import api
from service import stats, auth, user, res, tag, company, cheer, setting
import urllib.request
import urllib.error
import base64

# resource関連のロード
api_host = config.api_host
g_greeting = json.load(open("./resource/greeting.json", mode='r', encoding='utf-8'))

app = Flask(__name__)
app.secret_key = 'hoge'
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

# load routing
app.register_blueprint(reset.app)
app.register_blueprint(manabu.app)
app.register_blueprint(contact.app)
app.register_blueprint(mypage.app)
app.register_blueprint(news.app)
app.register_blueprint(api.app)
app.register_blueprint(profile.app)
app.register_blueprint(ranking.app)
app.register_blueprint(settings.app)
app.register_blueprint(companys.app)
app.register_blueprint(setting_news.app)
app.register_blueprint(question.app)
app.register_blueprint(policy.app)
app.register_blueprint(pageError.app)
app.register_blueprint(knowledge.app)
app.register_blueprint(introduction.app)
app.register_blueprint(target.app)
app.register_blueprint(activities.app)
app.register_blueprint(event.app)

@app.template_filter('n2br')
def n2br(arg):
    return Markup(arg.replace('\n', '<br>'))

@login_manager.user_loader
def load_user(user_id):
    result = user.fetchUserProfile(user_id)
    tmp_displayName = result['data']['displayName']
    email = result['data']['username']
    return User(user_id, tmp_displayName, email)

@app.route("/")
def index():
    return render_template('ver2.1/pages/login.html')

@app.route('/knowledge_count',methods=['Get'])
def getKnowledgeCount():
    count = stats.questioncount()
    return json.dumps(count)

@app.route("/login", methods=["GET", "POST"])
def login():
    if(request.method == "POST"):
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        username = data["name"]
        password = data["password"]
        result = auth.login(username, password)
        tmp_authentication = result["authentication"]
        profileResult = ""

        if tmp_authentication:
            tmp_userId = result["userId"]
            tmp_displayName = username

            profileResult = user.fetchUserProfile(tmp_userId)
            count = stats.questioncount()
            email = profileResult['data']['username']
            login_user(User(tmp_userId, tmp_displayName, email))
            result['profilePicture'] = profileResult['data']['profilePicture']
            result['displayName'] = profileResult['data']['displayName']
            result['questionCount'] = count['data']
        return json.dumps(result)
    else:
        try:
            userId = current_user.id
            logined = True
        except:
            logined = False

        if logined:
            return redirect(url_for('home'))
        else:
            return render_template('login.html', methods=["GET", "POST"])

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route("/home/")
# @config.kbauth.login_required
def ver2_home():
    if current_user.is_authenticated:
        userId = current_user.id
        return render_template('ver3/home/index.html')
    else:
        return redirect(url_for('index'))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if(request.method == "POST"):
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        email = data['email']
        userName = data['username']
        password = data['password']
        retypepassword = data['retypepassword']
        token = data['token']
        if password == retypepassword:
            result = user.signup(email, password, userName,token)
            if result['result'] == "success":
                tmp_userId = result["userId"]
                tmp_displayName = userName
                login_user(User(tmp_userId, tmp_displayName,email))
                result['profilePicture'] = ''
                result['displayName'] = userName
                return json.dumps(result)
            else:
                return render_template('ver2.1/pages/signup.html', message="Password not match")
        else:
            return render_template('ver2.1/pages/signup.html', message="Invalid user")

    else:
        mail = str(request.args.get("key1", "asukakirara@idealump.com"))
        # m1=m.replace("{", '')
        # mail=m1.replace("}", '')
        mail = decodeMail(mail)
        token = str(request.args.get("key2"))
        #token = (token.replace("{", '')).replace("}", '')
        status = auth.checkInviteToken(token) #status = true is ok for signup
        if status['data']:
            return render_template('ver2.1/pages/signup.html',mail=mail, token=token)
        else:
            return render_template('ver2.1/page_error/sessionExpire.html')

def decodeMail(mail):

    base64_message = str(mail)
    base64_bytes = base64_message.encode()
    message_bytes = base64.b64decode(base64_bytes)
    mailText = message_bytes.decode()
    return mailText

@app.errorhandler(404)
def error_404(error):
    #return render_template('404.html'), 404
    return redirect(url_for('index'))

@app.errorhandler(500)
def error_handler(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host=config.host_name, port=config.port,debug=True)
    #app.run(host='0.0.0.0',port=5000, debug=True)
