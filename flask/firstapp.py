from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "My First Flask App"

app.run(debug=True)