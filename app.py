# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import markovify
import random
import os

app = Flask(__name__)

setOfPrefacingTemplates = [
  "Good question: %(issue)s is a contentious issue.",
  "%(issue)s, eh. I was hoping you'd ask me that.",
  "I normally don't like to talk about %(issue)s, but I'll do you a favor this one time.",
  "I mean is %(issue)s really that relevant? Especially in the context of this discussion?",
  "I have my own personal opinions about %(issue)s, but within my capacity as President, here's what I think:"
]

@app.route('/chat', methods=["GET"])
def index():

  prefacingText = ""

  if request.args.get('issue') != None:
    issue = unicode(request.args.get('issue'))
    prefacingText = (setOfPrefacingTemplates[random.randint(0, len(setOfPrefacingTemplates) - 1)] % locals())

  newSpeech = ""

  with open('raw.txt') as f:
    rawText = f.read()

  model = markovify.Text(rawText, state_size=3)

  for i in range(1):
    newSpeech += " " + model.make_short_sentence(140)

  return jsonify({
    "content": newSpeech,
    "prefacingText": prefacingText
  })

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
