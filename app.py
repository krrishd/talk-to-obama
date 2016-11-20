# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import markovify
import random
import os

def is_int(input):
  try:
    num = int(input)
  except ValueError:
    return False
  return True

app = Flask(__name__)
CORS(app)

setOfPrefacingTemplates = [
  "Good question: %(issue)s is a contentious issue. Here's what Obama says:",
  "%(issue)s, eh. He was hoping you'd ask that.",
  "He normally doesn't like to talk about %(issue)s, but he'll make an exception this one time.",
  "I mean is %(issue)s really that relevant? Obama will make an exception just this once.",
  "He has his own personal opinions about %(issue)s, but within his capacity as President, here's what he thinks:"
]

@app.route('/chat', methods=["GET", "OPTIONS"])
@cross_origin()
def index():

  prefacingText = ""
  size = ""

  if request.args.get('issue') != None:
    issue = unicode(request.args.get('issue'))
    prefacingText = (setOfPrefacingTemplates[random.randint(0, len(setOfPrefacingTemplates) - 1)] % locals())

  if request.args.get('size') != None:
    size = unicode(request.args.get('size'))

  newSpeech = ""

  with open('allspeeches.txt') as f:
    rawText = f.read()

  model = markovify.Text(rawText, state_size=3)

  if size == "":
    for i in range(2):
      if (i > 0):
        newSpeech += " "
      newSpeech += model.make_sentence()
  elif size == "tweet":
    newSpeech += model.make_short_sentence(140)
  elif is_int(size):
    for i in range(int(size)):
      if (i > 0):
        newSpeech += " "
      newSpeech += model.make_sentence()

  return jsonify({
    "content": newSpeech,
    "prefacingText": prefacingText
  })

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
