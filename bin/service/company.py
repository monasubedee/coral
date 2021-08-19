import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"


# def fetchTeam(userId):
#     req = urllib.request.Request(
#         (api_host + "/company_teams/get?userId=" + userId), method="GET")
#     with urllib.request.urlopen(req) as res:
#         response_body = res.read().decode("utf-8")
#     return json.loads(response_body)
#
#
# def fetchPosition(companyCode):
#     req = urllib.request.Request(
#         (api_host + "/company_positions/get?companyCode=" + companyCode), method="GET")
#     with urllib.request.urlopen(req) as res:
#         response_body = res.read().decode("utf-8")
#     return json.loads(response_body)

def CompanyInformationRegister(data):
    obj = json.dumps(data).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/company/companyInformation/register"), data=obj, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        res = json.loads(response_body)
    return res

def fetchCompanyInfo(userId):
    req = urllib.request.Request(
        (api_host + "/company/companyInformation/get?userId=" + str(userId)), method="GET")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)

# def CompanyInformationRegister(companyname,postalno,residence,street,cityname,fulladd,building,phoneno,companyurl,respname,respmail,respposition,billingname,b_postalno,b_residence,b_street,b_cityname,b_fulladd,b_building,userId):
#
#     obj = {
#         "companyname":companyname,
#         "postalno":postalno,
#         "residence":residence,
#         "street":street,
#         "cityname":cityname,
#         "fulladd":fulladd,
#         "building":building,
#         "phoneno":phoneno,
#         "companyurl":companyurl,
#         "respname":respname,
#         "respmail":respmail,
#         "respposition":respposition,
#         "billingname":billingname,
#         "b_postalno":b_postalno,
#         "b_residence":b_residence,
#         "b_street":b_street,
#         "b_cityname":b_cityname,
#         "b_fulladd":b_fulladd,
#         "b_building":b_building,
#         "userId" : userId
#     }
#     # print("hello")
#
#     # print(obj)
#
#     json_data = json.dumps(obj).encode("utf-8")
#     headers = {"Content-Type": "application/json"}
#     req = urllib.request.Request(
#         (api_host + "/companyInformation/register"), data=json_data, method="POST", headers=headers)
#     with urllib.request.urlopen(req) as res:
#         response_body = res.read().decode("utf-8")
#         res = json.loads(response_body)
#     return res
