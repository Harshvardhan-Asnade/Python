from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to THE Website <h1>" 
            

@app.route("/about")
def bbout():
    return "Your are in the About Page"

@app.route('/contact')
def contact():
    return "You are in the Contact Page"


if __name__=="__main__":
    app.run(debug=True)
