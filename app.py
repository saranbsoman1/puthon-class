from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "welcome"

@app.route("/home") 
def home():
    return "welcome to my homepage"   


if(__name__=="__main__"):
    app.run()