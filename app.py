from flask import *

app = Flask(__name__)


@app.route("/")
def game():
    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)