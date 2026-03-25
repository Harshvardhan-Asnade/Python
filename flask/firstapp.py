from flask import Flask

app=Flask(__name__)

@app.route("/")
def Home():
    return "<h1>Welcome to THE Website <h1>" 
            

@app.route("/about")
def About():
    return "Your are in the About Page"



if __name__=="__main__":
    app.run(debug=True)
