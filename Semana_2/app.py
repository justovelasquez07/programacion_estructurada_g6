from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    answer = ""

    if request.method == "POST":

        grade = int(request.form["txtGrade"])

        if grade >= 60:
            answer = "You get pass"
        else:
            answer = "Your learning is at an initial stage."

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)