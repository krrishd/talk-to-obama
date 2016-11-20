# talk-to-obama

Simple Flask server running a Markov chain off of Obama's speech transcripts, exposing random sentences at http://talk-to-obama.herokuapp.com/chat

## How To Use

You can deploy this like any Flask app, or if you'd like to use the hosted API, simply request the aforementioned `/chat` endpoint.

The endpoint takes two optional URL parameters, size and issue: `?size={Number || 'tweet'}` and `issue={String}`.

## Projects Using This:

* [Obama || Markov](http://guso.io/obama)
* [Obama Discord Bot](https://github.com/michaelmdresser/obama-discordbot)
* [Obama Meme Generator](https://github.com/michaelmdresser/obama-memegenerator)

