from flask import Flask, render_template
import sys
application = Flask(__name__)


@application.route("/")
@application.route("/home")
def home():
    return render_template('web.html')


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
