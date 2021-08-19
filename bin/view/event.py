from flask import Blueprint, render_template
from flask_login import current_user,login_required

app = Blueprint("event", __name__, url_prefix="/event")

@app.route("", methods=["GET"])
def index():
    return render_template('/ver3/event/index.html')
