
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    numbers = []

    for number in range(10):
        numbers.append(number)

    return render_template("index.html", numbers=numbers)

if __name__ == "__main__":
    app.run(debug=True)