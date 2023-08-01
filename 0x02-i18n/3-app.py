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
dir(babel)


@app.route('/')
def home():
    """root route for the app
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> Union[str, None]:
    """choose the best language for user from those we support
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run(debug=False)
