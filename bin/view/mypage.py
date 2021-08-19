from flask import Blueprint, render_template
from flask_login import login_required, current_user
from service import user, stats, res
import config

app = Blueprint("mypage", __name__, url_prefix="/mypage")


@app.route("/")
@login_required
# @config.kbauth.login_required
def mypage():

    # prepare api api_host param
    userId = current_user.id

    occupationsData = res.fetchOccupations()

    countriesData = res.fetchCountries()

    result = user.fetchUserProfile(userId)

    displayName = result['data']['displayName']
    hiredYear = result['data']['hireDate']
    birthDate = result['data']['birthDate']
    countryId = result['data']['countryId']
    languageSet = result['data']['languageSet']
    roles = result['data']['roles']
    skillSet = result['data']['skillSet']
    goal = result['data']['goal']
    occupationId = result['data']['occupationId']
    if result['data']['gender'] == 1:
        gender = '男'
    elif result['data']['gender'] == 2:
        gender = '女'
    else:
        gender = 'その他'

    # findOne ocupation label
    userOcupationList = list(
        filter(lambda dic: dic['id'] == occupationId, occupationsData['occupations']))
    ocupationLabel = userOcupationList[0]['label'] if len(
        userOcupationList) == 1 else ''

    # findOne country label
    userCountryList = list(
        filter(lambda dic: dic['id'] == countryId, countriesData['countries']))
    countryLabel = userCountryList[0]['label'] if len(
        userCountryList) == 1 else ''

    result = stats.fetchUserStats(userId)

    totalAnswerCount = result['data']['totalAnswerCount']
    totalCorrectRate = result['data']['totalCorrectRate']
    totalConsecutiveCorrectCount = result['data']['totalConsecutiveCorrectCount']
    totalConsecutiveLoginDayCount = result['data']['totalConsecutiveLoginDayCount']
    totalCreateQuestionCount = result['data']['totalCreateQuestionCount']
    totalDailyChallengeSuccessCount = result['data']['totalDailyChallengeSuccessCount']

    result = user.fetchFavedQuestions(userId)
    questionsClipped = list()
    if result['data'] == None:
        pass
    else:
        for entry in result['data'].values():
            questionsClipped.append(
                {'correct': entry['correct'], 'questionText': entry['questionText']})

    result = user.fetchAnswerdQuestions(userId)
    questionsAnswered = list()
    try:
        if len(result['data']) > 0:
            for entry in result['data'].values():
                questionsAnswered.append(
                    {'correct': entry['correct'], 'questionText': entry['questionText']})
        else:
            pass
    except:
        pass

    result = user.fetchCreatedQuestions(userId)
    questionsCreated = list()
    try:
        if len(result['data']) > 0:
            for entry in result['data'].values():
                questionsCreated.append(
                    {'correct': entry['correct'], 'questionText': entry['questionText'], 'questionId': entry['questionId']})
        else:
            pass
    except:
        pass

    #avatorImage = user.getAvatorImage(userId)

    data = {
        "displayName": displayName,
        "hiredYear": hiredYear,
        "birthDate": birthDate,
        "country": countryLabel,
        "languageSet": languageSet,
        "gender": gender,
        "occupation": ocupationLabel,
        "roles": roles,
        "skillSet": skillSet,
        "goal": goal,
        "totalAnswerCount": totalAnswerCount,
        "totalCorrectRate": totalCorrectRate,
        "totalConsecutiveCorrectCount": totalConsecutiveCorrectCount,
        "totalConsecutiveLoginDayCount": totalConsecutiveLoginDayCount,
        "totalCreateQuestionCount": totalCreateQuestionCount,
        "totalDailyChallengeSuccessCount": totalDailyChallengeSuccessCount
    }
    return render_template('mypage.html', data=data, questionsClipped=questionsClipped, questionsAnswered=questionsAnswered, questionsCreated=questionsCreated)


@app.route("/edit")
@login_required
def mypage_edit():
    userId = current_user.id

    # language list
    languageData = res.fetchLanguages()

    # country list
    countriesData = res.fetchCountries()

    # occupation list
    occupationsData = res.fetchOccupations()

    # user profile
    result = user.fetchUserProfile(userId)

    displayName = result['data']['displayName']
    hireDate = result['data']['hireDate']
    birthDate = result['data']['birthDate']
    countryId = result['data']['countryId']
    languageSet = result['data']['languageSet']
    roles = result['data']['roles']
    skillSet = result['data']['skillSet']
    goal = result['data']['goal']
    occupationId = result['data']['occupationId']
    if result['data']['gender'] == 1:
        gender = '男'
    elif result['data']['gender'] == 2:
        gender = '女'
    else:
        gender = 'その他'

    #avatorImage = user.getAvatorImage(userId)

    data = {
        "displayName": displayName,
        "hireDate": hireDate,
        "birthDate": birthDate,
        "countryId": countryId,
        "languageSet": languageSet,
        "gender": gender,
        "occupationId": occupationId,
        "roles": roles,
        "skillSet": skillSet,
        "goal": goal
    }

    return render_template('profile_edit.html', data=data, countries=countriesData['countries'], languageSet=languageData['languages'], occupations=occupationsData['occupations'])
