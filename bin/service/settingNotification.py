import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"

def fetchSettingNotification(hour,minute,notidays,holidayflag,userId):
    obj = {
        "hour": hour,
        "minute": minute,
        "notidays": notidays,
        "holidayflag":holidayflag,
        "userId": userId
    }
    json_data = json.dumps(obj).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        (api_host + "/settings/notification"), data=json_data, method="POST", headers=headers)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
        res = json.loads(response_body)
    return res
    # url = api_host + "/setting/notification"
    # method = "POST"
    # headers = {"Content-Type": "application/json"}
    # json_data = json.dumps(
    #     {"userId": userId, "hour": hour," minute": minute, "notidays": notidays,"holidayflag":holidayflag}).encode("utf-8")
    # req = urllib.request.Request(
    #     url, data=json_data, method=method, headers=headers)
    # with urllib.request.urlopen(req) as response:
    #     response_body = response.read().decode("utf-8")
    # return json.loads(response_body)
