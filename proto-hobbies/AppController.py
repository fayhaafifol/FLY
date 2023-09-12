from flask import Flask, render_template, request, redirect
from Model.database import Database

app = Flask(__name__)
database = Database()

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/GetProtons")
def getProtons():
    return render_template("protons.html", proton=database.protons)

@app.route("/GetHobbies")
def getHobbies():
    return render_template ("hobby.html" ,hobby=database.hobbies)

@app.route("/AddProtons")
def GetAddProton():
    return render_template ("add proton.html" , proton=database.protons)

@app.route("/AddHobbies")
def GetAddHobbies():
    return render_template ("add hobby.html" ,hobby=database.hobbies)

@app.route("/ViewProtons")
def GetViewProton():
    return render_template ("proton_view.html" , proton=database.protons)

@app.route("/ViewHobbies")
def GetViewHobbies():
    return render_template ("hobby_view.html" ,hobby=database.hobbies)

@app.route("/DeleteProtons")
def GetDeleteProton():
    return render_template ("delete p.html" , proton=database.protons)

@app.route("/DeleteHobbies")
def GetDeleteHobbies():
    return render_template ("delete h.html" ,hobby=database.hobbies)


@app.route("/AddProtons/add",methods=["POST"])
def addProton(protonName: str, protonAge: int, protonTrack: str):
        protonName = request.form.get("protonName")
        protonAge = request.form.get("protonAge")
        protonTrack= request.form.get("protonTrack")
        database.addProton(protonName,protonAge,protonTrack)
        return redirect("/AddProtons")

@app.route("/AddHobbies",methods=["POST"])
def addHobby(hobbyTitle: str, imagePAth: str):
        hobbyTitle = request.form.get("hobbyTitle")
        imagePAth = request.form.get("imgePAth")
        database.addHobby(hobbyTitle,imagePAth)
        return redirect("/AddHobbies")


@app.route("/ViewHobbies/<hobbyTitle>")
def viewHobby(hobbyTitle: str):
    database.findHobby(hobbyTitle)
    return redirect("/ViewHobbies")

@app.route("/ViewProtons/<protonName>")
def viewProton(protonName: str):
    database.findProton(protonName)
    return redirect("/ViewProtons")

@app.route("/DeleteHobbies/<hobbyTitle>",methods=["DELETE"])
def deleteHobby(hobbyTitle: str):
     hobbyTitle=request.form.get("hobbyTitle")
     database.deleteHobby(hobbyTitle)
     return redirect("/DeleteHobbies")

@app.route("/DeleteProtons/<protonName>",methods=["DELETE"])
def deleteProton(protonName: str):
     protonName=request.form.get("protonName")
     database.deleteProton(protonName)
     return redirect("/DeleteProtons")

app.run()
