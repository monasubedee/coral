from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import current_user,login_required
from email.mime.text import MIMEText
from service import user,contactRegister
import smtplib
import config
from datetime import datetime

app = Blueprint("contact", __name__, url_prefix="/contact")


@app.route("/", methods=["GET", "POST"])
# @config.kbauth.login_required
def contact():
    if current_user.is_authenticated:
        if request.method == 'GET':
            return render_template('/ver2.1/pages/contact.html')
        else:
            try:
                userId = current_user.id
                inquiry_msg = request.form["inquiry_msg_hidden"]
                result = user.fetchUserProfileForContact(userId)
                result = result['data']
                authority = result['authority']
                userName = result['username']
                userMail = result['email']
                companyName = result['companyName']
                position = result['position']
                team = result['team']
                # send a mail
                message = "<p>ログイン済みのユーザーからお問い合わせがありました。</p><br/>"
                message += "<p>会社名 : " + str(companyName) + "</p>"
                message += "<p>アカウント権限 : " + str(authority) + "</p>"
                message += "<p>役職 : " + str(position) + "</p>"
                message += "<p>チーム : " + str(team) + "</p>"
                message += "<p>名前 : " + str(userName) + "</p>"
                message += "<p>メールアドレス : " + str(userMail) + "</p>"
                message += "<p>お問い合わせ内容 :</p>"
                message += "<p>" + inquiry_msg + "</p>"

                msg = MIMEText(message, "html")
                msg["Subject"] = "ログイン済みのユーザーからお問い合わせがありました。"
                msg["To"] = "info@knowledge-bank.jp"
                #msg["To"] = "chitthushine.ucsy@gmail.com"
                msg["From"] = "no-reply@knowledge-bank.jp"
                account = "no-reply@knowledge-bank.jp"
                password = "lJ$ZJi3R"

                # サーバを指定する
                server = smtplib.SMTP("smtp22.gmoserver.jp", 587)
                server.login(account, password)
                server.send_message(msg)
                server.quit()
                #msg = contactRegister.saveContact(userId,inquiry_msg)

                #send message to client
                today = datetime.now()
                today = today.strftime('%Y/%m/%d %H:%M')
                messageClient = "<p>以下の内容でお問い合わせを受け付けました。</p><br/>"
                messageClient += "<p>日時 : " + str(today) + "</p><br/>"
                messageClient += "<p>会社名 : " + str(companyName) + "</p>"
                messageClient += "<p>アカウント権限 : " + str(authority) + "</p>"
                messageClient += "<p>役職 : " + str(position) + "</p>"
                messageClient += "<p>チーム : " + str(team) + "</p>"
                messageClient += "<p>名前 : " + str(userName) + "</p>"
                messageClient += "<p>メールアドレス : " + str(userMail) + "</p>"
                messageClient += "<p>お問い合わせ内容：</p>"
                messageClient += "<p>" + inquiry_msg + "</p><br/>"
                messageClient += """<p>---------------------------------<br/>
                お心当たりがない場合は、<br/>
                info@knowledge-bank.jp にお問い合わせください。<br/><p>
                <p>*******************************************************<br/>
                「楽しくためる、楽しくまなぶ」<br/>
    　           Knowledge Bank <br/>
                MAIL：<a href="info@knowledge-bank.jp">info@knowledge-bank.jp </a><br/>
                WEB：<a href="https://knowledge-bank.jp/">https://knowledge-bank.jp/</a>
                <p>
                ※このメールアドレスは送信専用です。<br/>
                ご返信いただきましてもお返事できませんので、ご了承ください。<br/>
                **********************************************************
                </p>"""

                msgClient = MIMEText(messageClient, "html")
                msgClient["Subject"] = "【Knowledge Bank】お問い合わせを受け付けました。"
                msgClient["To"] = str(userMail)
                msgClient["From"] = "no-reply@knowledge-bank.jp"
                account = "no-reply@knowledge-bank.jp"
                password = "lJ$ZJi3R"

                # サーバを指定する
                server = smtplib.SMTP("smtp22.gmoserver.jp", 587)
                server.login(account, password)
                server.send_message(msgClient)
                server.quit()

            except:
                abort(500)
        return render_template('ver2.1/pages/contact_done.html')
    else:
        return redirect(url_for('contact.contact_unlogin'))

@app.route("/unlogin", methods=["GET", "POST"])
def contact_unlogin():
    print("hello ",request.method)
    if request.method == 'GET':
        return render_template('/ver2.1/pages/contact_unlogin.html')
    else:
        try:
            print("hi")
            inquiry_msg = request.form["inquiry_msg_hidden"]
            companyName = request.form["company"]
            deptName = request.form["department"]
            fullName = request.form["name"]
            mail = request.form["email"]
            phone = request.form["tel"]
            # today = datetime.now()
            # today = today.strftime('%Y/%m/%d %H:%M')
            # send a mail
            message = "<p>未ログインのユーザーからお問い合わせがありました。</p><br/>"
            # message += "<p>日時 : " + str(today) + "</p><br/>"
            message += "<p>会社名 : " + str(companyName) + "</p>"
            message += "<p>部署名 : " + str(deptName) + "</p>"
            message += "<p>氏名 : " + str(fullName) + "</p>"
            message += "<p>電話番号 : " + str(phone) + "</p><br/>"
            message += "<p>メールアドレス : " + str(mail) + "</p>"
            message += "<p>お問い合わせ内容 :</p>"
            message += "<p>" + inquiry_msg + "</p>"

            msg = MIMEText(message, "html")
            msg["Subject"] = "未ログインユーザーからお問い合わせがありました。"
            msg["To"] = "info@knowledge-bank.jp"
            #msg["To"] = "chitthushine.ucsy@gmail.com"
            msg["From"] = "no-reply@knowledge-bank.jp"
            account = "no-reply@knowledge-bank.jp"
            password = "lJ$ZJi3R"

            # サーバを指定する
            server = smtplib.SMTP("smtp22.gmoserver.jp", 587)
            server.login(account, password)
            server.send_message(msg)
            server.quit()

            #send message to client
            today = datetime.now()
            today = today.strftime('%Y/%m/%d %H:%M')
            messageClient = "<p>以下の内容でお問い合わせを受け付けました。</p><br/>"
            messageClient += "<p>日時 : " + str(today) + "</p><br/>"
            messageClient += "<p>会社名 : " + str(companyName) + "</p>"
            messageClient += "<p>部署名 : " + str(deptName) + "</p>"
            messageClient += "<p>氏名 : " + str(fullName) + "</p>"
            messageClient += "<p>メールアドレス : " + str(mail) + "</p>"
            messageClient += "<p>電話番号 : " + str(phone) + "</p><br/>"
            messageClient += "<p>お問い合わせ内容：</p>"
            messageClient += "<p>" + inquiry_msg + "</p><br/>"
            messageClient += """<p>---------------------------------<br/>
            お心当たりがない場合は、<br/>
            info@knowledge-bank.jp にお問い合わせください。<br/><p>
            <p>*******************************************************<br/>
            「楽しくためる、楽しくまなぶ」<br/>
　           Knowledge Bank <br/>
            MAIL：<a href="info@knowledge-bank.jp">info@knowledge-bank.jp </a><br/>
            WEB：<a href="https://knowledge-bank.jp/">https://knowledge-bank.jp/</a>
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
        except:
            abort(500)
    return render_template('ver2.1/pages/contact_done_unlogin.html')
    # return render_template('ver2.1/pages/contact_done.html')
