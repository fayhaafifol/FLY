from flask import Flask, render_template, request, redirect
from Model.database import Database

app = Flask(__name__)
database = Database()

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/protons")
def getProtons():
    return render_template("protons.html")

@app.route("/hobbies")
def getHobbies():
    return render_template (".html")

@app.route("/protons",methods="POST")
def addProton(protonName: str, protonAge: int, protonTrack: str):
        protonName = request.form.get("protonName")
        protonAge = request.form.get("protonAge")
        protonTrack= request.form.get("protonTrack")
        database.addProton(protonName,protonAge,protonTrack)
        return redirect("/protons")


@app.route("/hobbies",methods="POST")
def addHobby(hobbyTitle: str, imagePAth: str):
        hobbyTitle = request.form.get("hobbyTitle")
        imagePAth = request.form.get("imgePAth")
        database.addProton(hobbyTitle,imagePAth)
        return redirect("/hobbies")


@app.route("/hobbies/<hobbyTitle>/<protonName>")
def matchProtoHobby(hobbyTitle: str,protonName: str):
    #TODO
    pass

#Views the hobby title, image and protons who like it
@app.route("/hobbies/<hobbyTitle>")
def viewHobby(hobbyTitle: str):
    #TODO
    pass

@app.route("/hobbies/<hobbyTitle>",methods="DELETE")
def deleteHobby(hobbyTitle: str):
     hobbyTitle=request.form.get("hobby")
     database.deleteHobby(hobbyTitle)
     return redirect("/hobbies")


@app.route("/protons/<protonName>",methods="DELETE")
def deleteProton(protonName: str):
     protonName=request.form.get("protonName")
     database.deleteProton(protonName)
     return redirect("/protons")
