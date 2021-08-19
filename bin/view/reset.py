from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import current_user
from service import user
import json

app = Blueprint("reset", __name__, url_prefix="/reset")
app.secret_key = 'app secret key'
# @app.route("/", methods=["GET", "POST"])
# def reset():
#     if request.method == "GET":
#         pageTitle = 'パスワード再発行'
#         try:
#             userId = current_user.id
#             avatorImage = user.getAvatorImage(userId)
#             logined = 'true'
#         except:
#             userId = 0
#             avatorImage = ''
#             logined = 'false'
#         return render_template('reset.html', title=pageTitle, avatorImage=avatorImage, logined=logined)
#     else:
#         # userMail = request.form["userMail"]
#         # passReset=user.requestPasswordReset(userMail)
#         # return render_template(url_for('reset_confirm'))
#
#         return ''

@app.route("/", methods=["GET", "POST"])
def reset():
    if request.method == "GET":
        pageTitle = 'パスワード再発行'
        try:
            userId = current_user.id
            #avatorImage = user.getAvatorImage(userId)
            logined = 'true'
        except:
            userId = 0
            #avatorImage = ''
            logined = 'false'
        return render_template('ver2.1/pages/pwd_reminder.html', title=pageTitle, logined=logined)
    else:
        # userMail = request.form["userMail"]
        # passReset=user.requestPasswordReset(userMail)
        # return render_template(url_for('reset_confirm'))

        return ''

@app.route("/confirm", methods=["POST"])
def resetTest():
    session['flag'] = 1
    received_data = request.data
    received_data = received_data.decode('utf-8')
    data = json.loads(received_data)
    mail = data["mail"]

    # API access as wrapper
    passReset=user.requestPasswordReset(mail)
    # return render_template(url_for('reset_confirm'))

    return json.dumps(passReset)

@app.route("/confirm",methods=["GET"])
def reset_confirm():
    pageTitle = 'パスワード再発行'
    sess_flag = 0
    try:
        sess_flag = session['flag']
    except:
        sess_flag = 0
    if current_user.is_authenticated or sess_flag == 1:
        try:
            userId = current_user.id
            #avatorImage = user.getAvatorImage(userId)
            logined = 'true'
        except:
            userId = 0
            #avatorImage = ''
            logined = 'false'
        return render_template('ver2.1/pages/pwd_reminder_send.html', title=pageTitle, logined=logined)
    else :
        return redirect(url_for('reset.reset'))

@app.route("/setting", methods=['GET', 'POST'])
def reset_setting():
    if request.method == "GET":
        token = str(request.args.get("token", ""))
        pageTitle = 'パスワード再発行'
        try:
            userId = current_user.id
            #avatorImage = user.getAvatorImage(userId)
            logined = 'true'
        except:
            userId = 0
            #avatorImage = ''
            logined = 'false'
        return render_template('ver2.1/pages/pwd_reminder_input.html', title=pageTitle, logined=logined, token=token)
    else:
        session['reset_result'] = 1
        received_data = request.data
        received_data = received_data.decode('utf-8')
        data = json.loads(received_data)
        token = data["token"]
        userPass = data["password"]

        # API access as wrapper
        result=user.definePassword(userPass, token)

        return json.dumps(result)


@app.route("/result")
def reset_result():
    pageTitle = 'パスワード再発行'
    sess_flag = 0
    try:
        sess_flag = session['reset_result']
    except:
        sess_flag = 0
    if current_user.is_authenticated or sess_flag == 1:
        try:
            userId = current_user.id
            #avatorImage = user.getAvatorImage(userId)
            logined = 'true'
        except:
            userId = 0
            #avatorImage = ''
            logined = 'false'
        return render_template('ver2.1/pages/pwd_reminder_done.html', title=pageTitle,  logined=logined)
    else :
        return redirect(url_for('reset.reset'))
