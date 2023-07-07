from flask import Flask, render_template
import sys
application = Flask(__name__)


@application.route("/")
@application.route("/home")
def home():
    return render_template('index.html')


if __name__ == "__main__":
    application.run()
