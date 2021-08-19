from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import current_user
import config

app = Blueprint("policy", __name__, url_prefix="/policy")

@app.route("/", methods=["GET", "POST"])
# @config.kbauth.login_required
def policy():
    if current_user.is_authenticated:
        return render_template('/ver2.1/pages/policy.html')
    else:
        return redirect(url_for('policy.policy_unlogin'))

@app.route("/unlogin", methods=["GET"])
def policy_unlogin():
    if request.method == 'GET':
        return render_template('/ver2.1/pages/policy_unlogin.html')
