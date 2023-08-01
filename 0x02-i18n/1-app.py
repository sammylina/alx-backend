#!/usr/bin/env python3
"""Basic flask app
"""


from flask import Flask, render_template
from flask_babel import Babel


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
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
