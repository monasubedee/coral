from flask import Blueprint, render_template, request,json,abort
from flask_login import login_required, current_user
from service import news
import config

app = Blueprint("setting_news", __name__, url_prefix="/settings")

@app.route("/news", methods=["GET", "POST"])
# @config.kbauth.login_required
def hogehoge_list():
    if current_user.is_authenticated:
        userId=current_user.id

        url=str(request)
        if(url.find('settings')!= -1):
            isHomePage="0"
            newsList = news.getNews(userId,isHomePage)
        else:
            isHomePage="1"
            newsList = news.getNews(userId,isHomePage)
        status = request.args.get("status", "")
        return render_template('ver2.1/settings/setting_news.html', methods=["GET", "POST"], news = newsList,status=status)
    else:
        return redirect(url_for('index'))

@app.route("/news/create", methods=["GET", "POST"])
# @config.kbauth.login_required
def hogehoge_add():
    if current_user.is_authenticated:
        if request.method=='GET':
            return render_template('ver2.1/settings/setting_news_hogehoge.html')
        else:
            received_data = request.data
            received_data = received_data.decode('utf-8')
            data = json.loads(received_data)
            data['userId']=current_user.id
            result = news.registerNews(data.get('userId'), data.get('title'), data.get('description'), data.get('isPublished'))

            return json.dumps(result)
    else:
        return redirect(url_for('index'))

@app.route("/news/edit", methods=["GET", "POST"])
# @config.kbauth.login_required
def hogehoge_edit():
    if current_user.is_authenticated:
        if request.method=='POST':
            received_data = request.data
            received_data = received_data.decode('utf-8')
            data = json.loads(received_data)
            data['userId']=current_user.id
            result = news.editNews(data.get('userId'), data.get('title'), data.get('description'), data.get('isPublished'),data.get('noticeId'))
            return json.dumps(result)
        else:
            return render_template('ver2.1/settings/setting_news_hogehoge.html')
        #return redirect(url_for('index'))

@app.route("/news/id", methods=["GET"])
# @config.kbauth.login_required
def hogehoge_findid():
    if current_user.is_authenticated:
        if request.method=='GET':
            id = int(request.args.get("id",0))
            res = news.findId(id)
            return json.dumps(res)
    else:
        return redirect(url_for('index'))

@app.route('/newslist_delete', methods=["POST"])
# @config.kbauth.login_required
def newslistdelete():
    if current_user.is_authenticated:
        try:
            received_data = request.data
            received_data = received_data.decode('utf-8')
            data = json.loads(received_data)
            msg = news.news_list_delete(data)

        except:
            return abort(500)
        return json.dumps(msg)
    else:
        return redirect(url_for('index'))
