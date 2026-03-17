from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", name="Harsh")

app.run(debug=True, port=5001)