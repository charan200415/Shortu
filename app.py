import flask
import requests
app = flask.Flask(__name__)

@app.route("/")  # now the subdomain will be passed into the parameter 'username'
def profile():
    print("working")
    return flask.request.url
    

@app.route("/test")  # now the subdomain will be passed into the parameter 'username'
def test():
    return "Hello Test Passed !"
