from flask import Flask, render_template,request, session,redirect
from threading import Thread
from oauth import Oauth

app = Flask(__name__)

@app.route('/')
def home():
    return "h"

@app.route("/login")
def login():
	return redirect("youtube.com")


def run():
  app.run(host='0.0.0.0',port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
