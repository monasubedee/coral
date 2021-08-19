from flask import Blueprint, render_template, request, redirect, url_for,json, abort
from flask_login import current_user,login_required
from service import company
import config

app = Blueprint("companys", __name__, url_prefix="/settings")

@app.route('/companyInfo',methods=["GET"])
# @config.kbauth.login_required
def company_info():
    if current_user.is_authenticated:
        try:
            userId=current_user.id
            res = company.fetchCompanyInfo(userId)
            return json.dumps(res)
        except:
            return abort(500)
    else:
        return redirect(url_for('index'))

@app.route('/company', methods=["GET","POST"])
# @config.kbauth.login_required
def base_company():
    if current_user.is_authenticated:
        if request.method == "GET":
            return render_template('ver2.1/pages/company.html')
        else:
            try:
                received_data = request.data
                received_data = received_data.decode('utf-8')
                data = json.loads(received_data)
                data['userId']=current_user.id
                msg = company.CompanyInformationRegister(data)
                return json.dumps(msg)
            except:
                return abort(500)
    else:
        return redirect(url_for('index'))
