from flask import Blueprint, render_template, request, redirect, url_for,json, abort
from flask_login import current_user,login_required
from service import activity
import config

app = Blueprint("activity", __name__, url_prefix="/activity")

@app.route("/", methods=["GET"])
#@config.kbauth.login_required
def activity_list():
    if current_user.is_authenticated:
        userId = current_user.id
        activityList = activity.getActivityList(userId)
        return json.dumps(activityList)
    else:
        return redirect(url_for('index'))
