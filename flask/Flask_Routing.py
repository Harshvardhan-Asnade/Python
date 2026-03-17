from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"
@app.route("/user/<name>")
def user(name):
    return "Hello " + name
@app.route("/about")
def about():
    return "About Page"

app.run(debug=True)