from flask import Blueprint, render_template, request, redirect, url_for, abort
import config

app = Blueprint("knowledge", __name__, url_prefix="/knowledge")

@app.route("/", methods=["GET", "POST"])
# @config.kbauth.login_required
def knowledge():
        return render_template('/ver2.1/pages/knowledge.html')
