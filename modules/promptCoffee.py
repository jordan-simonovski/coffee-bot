import slackConnector
import random
import os
from datetime import *
import pytz

tz = pytz.timezone("Australia/Sydney")

coffeePlaces = ["Cafe XXII","La Tienda Cafe","harris.miller","Le Trader","the Nespresso Machine", "that Cafe on Level 3", "Bar Zini"]
coffeeGifs = [
        "https://media.giphy.com/media/l0MYAqn2iVLPTRGUw/giphy.gif",
        "https://media.giphy.com/media/l0MYAqn2iVLPTRGUw/giphy.gif",
        "https://media.giphy.com/media/oZEBLugoTthxS/giphy.gif",
        "https://media.giphy.com/media/zJ8ldRaGLnHTa/giphy.gif",
        "https://media.giphy.com/media/687qS11pXwjCM/giphy.gif",
        "https://media.giphy.com/media/10sKNgit3jiU2A/giphy.gif",
        "https://media.giphy.com/media/ceeFbVxiZzMBi/giphy.gif",
        "https://media.giphy.com/media/NJokhR7GCs0uY/giphy.gif",
        "https://media.giphy.com/media/R1fqW7QTkR8je/giphy.gif",
        "https://media.giphy.com/media/R5MzmBwjgu7UA/giphy.gif",
        "https://media.giphy.com/media/c2Enke05DX6F2/giphy.gif",
        "https://media.giphy.com/media/V3MlKQ1G0pV3G/giphy.gif",
        "https://media.giphy.com/media/zVcSYlq1DqTYs/giphy.gif",
        "https://media.giphy.com/media/NHUONhmbo448/giphy.gif",
        "https://media.giphy.com/media/5xaYLxI6riEuY/giphy.gif",
        "https://media.giphy.com/media/l2JI4zgwXw5IfyssE/giphy.gif",
        "https://media.giphy.com/media/xThuWjDsB8IbJggCME/giphy.gif",
        "https://media.giphy.com/media/11Lz1Y4n1f2j96/giphy.gif",
        "https://media.giphy.com/media/4WpvHyRMXCoww/giphy.gif",
        "https://media.giphy.com/media/13Y7TygzhUgT28/giphy.gif",
        "https://media.giphy.com/media/xTiTnLIpvL5o1tBy5W/giphy.gif",
        "https://media.giphy.com/media/xUySTv9gnqA5rDCKWs/giphy.gif",
        "https://media.giphy.com/media/oj05uAreWGy8U/giphy.gif",
        "https://media.giphy.com/media/3o6MbaY2SJYZvHctMY/giphy.gif",
        "https://media.giphy.com/media/oAzEHPyMlMHXW/giphy.gif",
        "https://media.giphy.com/media/w9XH7o9BbuLok/giphy.gif",
        "https://media.giphy.com/media/uAtUk9luIYL1C/giphy.gif",
        "https://media.giphy.com/media/7hLRKL65FxCuY/giphy.gif",
        "https://media.giphy.com/media/6n7d5NJoCSKfS/giphy.gif",
        "https://media.giphy.com/media/F6d5oNpTLssQ8/giphy.gif"
        ]

questions = [
        "It's that time of the day for some coffee from {0}",
        "Coffee? \n I hear {0} does great coffee.",
        "Who wants some caffeinated goodness from {0}",
        "{0}. You guys in?",
        "Coffee comrades! \n Time for some coffee from {0}",
        "COFFEE, COFFEE, COFFEE, COFFEE, COFFEE, COFFEE! \n Let's go to {0}",
        "Nothing like having some warm, creamy coffee slide down your throat at {0}",
        "Guise. Time. For. Coffee. \n {0}?",
        "Oh would you look at the time? \n It looks like it's time for some coffee from {0}",
        "What's that in your hands? \n It's not coffee. Maybe you should get some from {0}",
        "Ding ding ding! Coffee Time! \n You should check out {0} today.",
        "Coffee. {0}. Nuff said.",
        "Hey you guys wanna go get some coffee? I'm thinking {0} today.",
        "Need. Coffee. \n Brain no worky. \n Go to {0}"
	]

def checkDay():
    today = datetime.now(pytz.utc)
    localisedToday = today.astimezone(tz)
    return localisedToday.strftime("%A")

def askQuestion():
    coffeeGif = random.choice(coffeeGifs)
    day = checkDay()
    if day in dayActions:
        slackConnector.sendMessage(dayActions[day], coffeeGif)
    else:
        cafe = random.choice(coffeePlaces)
	question = random.choice(questions)
	slackConnector.sendMessage(question.format(cafe), coffeeGif)

dayActions = {
        "Tuesday": "Cheap Tuesdays at Antidote. Go go go!"
}
