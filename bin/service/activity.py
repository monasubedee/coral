import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v2"

def getActivityList(userId):
    method = "GET"
    url = api_host + "/stats/activity?&userId="+str(userId)

    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)
