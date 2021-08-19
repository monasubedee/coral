from flask import Blueprint, render_template, request, redirect, url_for, abort, jsonify, json
from flask_login import current_user,login_required
from email.mime.text import MIMEText
from service import user,contactRegister
import smtplib, json
from datetime import datetime
import config

app = Blueprint("introduction", __name__, url_prefix="/introduction")

@app.route('/')
# @config.kbauth.login_required
def introduction():
    return render_template('ver2.1/introduction/index.html')

@app.route('/news/1/')
# @config.kbauth.login_required
def introduction_news1():
    return render_template('ver2.1/introduction/news/1/index.html')

@app.route('/news/2/')
# @config.kbauth.login_required
def introduction_news2():
    return render_template('ver2.1/introduction/news/2/index.html')

@app.route('/news/3/')
# @config.kbauth.login_required
def introduction_news3():
    return render_template('ver2.1/introduction/news/3/index.html')

@app.route('/news/4/')
# @config.kbauth.login_required
def introduction_news4():
    return render_template('ver2.1/introduction/news/4/index.html')

@app.route("/contact/", methods=["GET", "POST"])
# @config.kbauth.login_required
def introduction_contact():

    if request.method == 'GET':
        return render_template('/ver2.1/introduction/contact/index.html')
    else:
        try:
            received_data = request.data
            received_data = received_data.decode('utf-8')
            data = json.loads(received_data)
            inquiry_msg = data["inquiry_msg"]
            companyName = data ["companyName"]
            deptName = data ["deptName"]
            fullName = data ["fullName"]
            mail = data ["mail"]
            phone = data ["phone"]
            today = datetime.now()
            today = today.strftime('%Y/%m/%d %H:%M')
            # send a mail
            message = "<p>以下のお問い合わせがありました。</p><br/>"
            message += "<p>日時 : " + str(today) + "</p><br/>"
            message += "<p>会社名 : " + str(companyName) + "</p>"
            message += "<p>部署名 : " + str(deptName) + "</p>"
            message += "<p>氏名 : " + str(fullName) + "</p>"
            message += "<p>メールアドレス : " + str(mail) + "</p>"
            message += "<p>電話番号 : " + str(phone) + "</p><br/>"
            message += "<p>お問い合わせ内容 :</p>"
            message += "<p>" + inquiry_msg + "</p>"

            msg = MIMEText(message, "html")
            msg["Subject"] = "LPからお問い合わせが来ました。"
            msg["To"] = "info@knowledge-bank.jp"
            msg["From"] = "no-reply@knowledge-bank.jp"
            account = "no-reply@knowledge-bank.jp"
            password = "lJ$ZJi3R"

            # サーバを指定する
            server = smtplib.SMTP("smtp22.gmoserver.jp", 587)
            server.login(account, password)
            server.send_message(msg)
            server.quit()
            #send message to client
            messageClient = "<p>以下の内容でお問い合わせを受け付けました。</p><br/>"
            messageClient += "<p>日時 : " + str(today) + "</p><br/>"
            messageClient += "<p>会社名 : " + str(companyName) + "</p>"
            messageClient += "<p>部署名 : " + str(deptName) + "</p>"
            messageClient += "<p>氏名 : " + str(fullName) + "</p>"
            messageClient += "<p>メールアドレス : " + str(mail) + "</p>"
            messageClient += "<p>電話番号 : " + str(phone) + "</p><br/>"
            messageClient += "<p>お問い合わせ内容 :</p>"
            messageClient += "<p>" + inquiry_msg + "</p><br/>"
            messageClient += """<p>---------------------------------<br/>
            お心当たりがない場合は、<br/>
            info@knowledge-bank.jp <br/>
            にお問い合わせください。<br/><p>
            <p>*******************************************************<br/>
            「楽しくためる、楽しくまなぶ」<br/>
　           Knowledge Bank <br/>
            MAIL：info@knowledge-bank.jp <br/>
            WEB：https://knowledge-bank.jp/</p>
            <p>
            ※このメールアドレスは送信専用です。<br/>
            ご返信いただきましてもお返事できませんので、ご了承ください。<br/>
            **********************************************************
            </p>"""

            msgClient = MIMEText(messageClient, "html")
            msgClient["Subject"] = "【Knowledge Bank】お問い合わせを受け付けました。"
            msgClient["To"] = str(mail)
            msgClient["From"] = "no-reply@knowledge-bank.jp"
            account = "no-reply@knowledge-bank.jp"
            password = "lJ$ZJi3R"

            # サーバを指定する
            server = smtplib.SMTP("smtp22.gmoserver.jp", 587)
            server.login(account, password)
            server.send_message(msgClient)
            server.quit()
            res = {
                "result": "ok",
                "message": "email has been sent.",
            }
            return jsonify(res)
        except:
            abort(500)

@app.route("/contact/thanks/", methods=["GET"])
# @config.kbauth.login_required
def introduction_contact_thanks():
    return render_template('ver2.1/introduction/contact/thanks/index.html')
