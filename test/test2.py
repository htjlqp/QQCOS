from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth
app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

weibo = oauth.remote_app(
    'weibo',
    consumer_key='1523741413',
    consumer_secret='dadfdcb4d08fa3825b951086c67d2e65',
    request_token_params={'scope': 'email,statuses_to_me_read'},
    base_url='https://api.weibo.com/2/',
    authorize_url='https://api.weibo.com/oauth2/authorize',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://api.weibo.com/oauth2/access_token',
    # since weibo's response is a shit, we need to force parse the content
    content_type='application/json',
)
@app.route('/')
def index():
    if 'oauth_token' in session:
        access_token = session['oauth_token'][0]
        resp = weibo.get('statuses/home_timeline.json')
        return jsonify(resp.data)
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return weibo.authorize(callback=url_for('authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))

if __name__ == '__main__':
    app.run()