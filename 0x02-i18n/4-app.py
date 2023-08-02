#!/usr/bin/env python3
"""Basic flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Union


app = Flask(__name__)


class Config(object):
    """app configuration constants
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """root route for the app
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """choose the best language for user from those we support
    """
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
