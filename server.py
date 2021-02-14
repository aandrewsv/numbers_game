from types import ClassMethodDescriptorType
from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)  
app.secret_key = "admin"

@app.route("/")
def index():
    if "random_num" not in session:
        session["random_num"] = random.randint(1,100)
        return render_template("index.html", landpage=True)
    if "input_num" in session:
        landpage = False
        if int(session["random_num"]) > int(session["input_num"]):
            toolow = True
        else:
            toolow = False
        if int(session["random_num"]) < int(session["input_num"]):
            toohigh = True
        else:
            toohigh = False
        if int(session["random_num"]) == int(session["input_num"]):
            correct = True
        else:
            correct = False
        return render_template("index.html", landpage=landpage, toolow=toolow,toohigh=toohigh,correct=correct)
    else:
        return render_template("index.html", landpage=True)

@app.route("/submit/", methods=['POST'])
def submit():
    session["input_num"] = request.form["number_input"]
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
