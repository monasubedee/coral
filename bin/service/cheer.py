import random
import json
import datetime

g_greeting = json.load(open("./resource/greeting.json", 'r'))


# cheer message creator
# 3-6: 朝早いですね！
# 6-9: おはようございます！
# 9-18:こんにちは！
# 18-3:こんばんは！
def createGreeting(hour, userName):
    if 3 <= hour and hour < 6:
        return '朝早いですね！' if userName == '' else userName + ' さん、朝早いですね！'
    elif 6 <= hour and hour < 9:
        return 'おはようございます！' if userName == '' else userName + ' さん、おはようございます！'
    elif 9 <= hour and hour < 18:
        return 'こんにちは！' if userName == '' else userName + ' さん、こんにちは！'
    else:
        return 'こんばんは！' if userName == '' else userName + ' さん、こんばんは！'


def choiceCheerMessageObject():
    return random.choice(g_greeting)
