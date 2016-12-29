#from eve import Eve

#app = Eve()
#
#if __name__ == '__main__':
#    app.run()
#!flask/bin/python
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

cards = json.load(open('AllCards.json'))



@app.route('/')
def index():
    return "Hello, World!"

@app.route('/card/all', methods=['GET'])
def servecards():
    return jsonify({'cards':cards})

@app.route('/card/search',methods=['POST'])
def serveSingleCard():
    print "Hello!"
    if request.data:
        print "Hi I'm hurr"
        raw_data = request.data
        print raw_data
    else:
        print "No request object."
    print "about to load json"
    data = json.loads(raw_data)
    print "JSON loaded - about to assign wantedCard"
    wantedCard = data['card']
    print "here is the card we want: " + str(wantedCard)
    returnCard = cards[str(wantedCard)]
    return str(returnCard)
    

if __name__ == '__main__':
    app.run(debug=True)
