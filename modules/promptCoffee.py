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
        "https://media.giphy.com/media/zVcSYlq1DqTYs/giphy.gif"
        ]

questions = [
        "It's that time of the day for a some coffee from {0}",
        "Coffee? I hear {0} does great coffee.",
        "Who wants some caffeinated goodness from {0}",
        "{0}. You guys in?",
        "Coffee comrades! Time for some coffee from {0}",
        "Nothing like having some warm, creamy coffee slide down your throat at {0}",
        "COFFEE, COFFEE, COFFEE, COFFEE, COFFEE, COFFEE! Let's go to {0}",
        "Guise. Time. For. Coffee. \n {0}?",
        "Oh would you look at the time? It looks like it's time for some coffee from {0}"
	]

def checkDay():
    today = datetime.now(pytz.utc)
    localisedToday = today.astimezone(tz)
    print(localisedToday)

def askQuestion():
        checkDay()
        coffeeGif = random.choice(coffeeGifs)
        cafe = random.choice(coffeePlaces)
	question = random.choice(questions)
	slackConnector.sendMessage(question.format(cafe), coffeeGif)
