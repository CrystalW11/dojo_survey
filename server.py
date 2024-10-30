from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "This is a secret key"

@app.get("/")
def index():

    return render_template("index.html")

@app.post("/process_form")
def process_form():

    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect("/results")


@app.get("/results")
def results():

    name = session["name"]
    location = session["location"]
    language = session["language"]
    comment = session["comment"]
    return render_template("results.html", name=name, location=location, language=language, comment=comment)

@app.route("/reset", methods=["GET"])
def reset():
    session.clear()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
