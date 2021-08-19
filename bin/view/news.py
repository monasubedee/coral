from flask import Blueprint, render_template, request, jsonify,json, url_for, redirect
from flask_login import login_required, current_user
from service import news, setting
import config

app = Blueprint("news", __name__, url_prefix="/news")
@app.route("/", methods=["GET", "POST"])
# @config.kbauth.login_required
def hogehoge_list():
    if current_user.is_authenticated:
        userId=current_user.id
        url=str(request)
        if(url.find('settings')!= -1):
            isHomePage="1"
            newsList = news.getNews(userId,isHomePage)
        else:
            isHomePage="0"
            newsList = news.getNews(userId,isHomePage)

        return render_template('ver2.1/news/news.html', methods=["GET", "POST"], news = newsList)
    else:
        return redirect(url_for('index'))

# @app.route("/news/hogehoge(add)", methods=["GET", "POST"])
# def hogehoge_add():
#     if(request.method == "POST"):
#         title = request.form["title"]
#         description = request.form["description"]
#         userId = current_user.id
#         isPublished = '1'
#         result = news.registerNews(userId, title, description, isPublished)


@app.route("/detail", methods=["GET"])
def news_detail():
    if current_user.is_authenticated:
        userId = current_user.id
        newsId=int(request.args.get("id", 0))
        successMsg=news.getNewsDetail(newsId,userId)
        return render_template("ver2.1/news/news_hogehoge.html", message=successMsg)
    else:
        return redirect(url_for('index'))

@app.route("/list", methods=["GET"])
def news_list():
    if current_user.is_authenticated:
        userId = current_user.id
        isHomePage="1"
        newsList = news.getNews(userId,isHomePage)
        return json.dumps(newsList)
    else:
        return redirect(url_for('index'))
