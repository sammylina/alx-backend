#!/usr/bin/env python3
"""Basic flask app
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """root route for the app
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
