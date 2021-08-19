import config
import urllib.request
import json
import urllib.error

api_host = config.api_host+"/api/v1"


def fetchLanguages():
    # api access 1
    url = api_host + "/res/languages"
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchCountries():
    url = api_host + "/res/countries"
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)


def fetchOccupations():
    url = api_host + "/res/occupations"
    method = "GET"
    req = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(req) as res:
        response_body = res.read().decode("utf-8")
    return json.loads(response_body)
