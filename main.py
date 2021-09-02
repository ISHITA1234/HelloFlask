from flask import Flask, render_template, request, redirect, url_for, session
import re

app = Flask(__name__)


@app.route('/pythonlogin/')
def login():
    msg = 'Hello All'
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.run()
