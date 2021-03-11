"""
# here starts the journey of web app
1. Make a simple login website
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

