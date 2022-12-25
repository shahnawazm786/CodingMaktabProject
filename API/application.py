from flask import flask
app=flask(__name__)

@app.route('/')
def index():
    return 'Hello!!! World'
