import requests
import json
import os

slackWebhook = os.environ.get('slack_webhook')

def buildMessage(question, imageUrl):
	slackMessage = {
		"response_type": "in_channel",
		"attachments": [{
			"text": question,
			"color": "#3AA3E3",
			"attachment_type": "default",
                        "image_url": imageUrl
		}]
	}
	return json.dumps(slackMessage)

def sendMessage(question, imageUrl):
	slackMessage = buildMessage(question, imageUrl)
	response = requests.post(slackWebhook, data=slackMessage)
