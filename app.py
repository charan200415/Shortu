import flask
import requests
app = flask.Flask(__name__)

@app.route("/")  # now the subdomain will be passed into the parameter 'username'
def profile():
    url=(flask.request.url).replace('.shortu.ml/','').replace('https://','')
    ret=requests.get(f'https://shortu.ml/{url}?Pa=djgkfdghbfgbghkfndgkjnfghknkjghnkjdghkjn').text
    if ret=='Not Found':
        return flask.redirect(f'https://shortu.ml/{url}')
    else:
        return flask.redirect(ret)

@app.route("/test")  # now the subdomain will be passed into the parameter 'username'
def test():
    return "Hello Test Passed !"
