import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"


def fetchTag(userId):
    req = urllib.request.Request((api_host + "/question/tag/get?userId="+str(userId)), method="GET")
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)
