from flask import Flask, jsonify, json
from flask import request
from modules import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def lambda_handler(event=None, context=None):
    return ""

def gimmeCoffee(req, res):
	promptCoffee.askQuestion()
	return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
