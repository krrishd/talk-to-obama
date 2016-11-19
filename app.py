# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import markovify
import random
import os

app = Flask(__name__)

@app.route('/chat', methods=["GET"])
def index():

  newSpeech = ""

  with open('raw.txt') as f:
    rawText = f.read()

  model = markovify.Text(rawText, state_size=1)

  for i in range(1):
    newSpeech += " " + model.make_short_sentence(140)

  return jsonify({
    "content": newSpeech
  })

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
