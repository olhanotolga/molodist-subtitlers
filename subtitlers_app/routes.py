from flask import Flask, render_template, url_for
from subtitlers_app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return "<h1>Oh yeah!</h1>"