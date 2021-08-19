from flask import Blueprint, render_template, request, redirect, url_for, abort

app = Blueprint("pageError", __name__, url_prefix="/pageError")

@app.route("/404", methods=["GET", "POST"])
def no_page_found():
    return render_template('/ver2.1/page_error/404.html')

@app.route("/500", methods=["GET", "POST"])
def inter_server_error():
    return render_template('/ver2.1/page_error/500.html')

@app.route("/503", methods=["GET", "POST"])
def under_construction():
    return render_template('/ver2.1/page_error/503.html')
