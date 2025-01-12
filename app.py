from flask import Flask, render_template, request
from cleaner import Cleaner

app = Flask(__name__)

arr = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        path = request.form["path"]
        ext = request.form["ext"]
        folder = request.form["folder"]

        global arr

        arr.append(path)
        arr.append(ext)
        arr.append(folder)

        clean = Cleaner(path,[folder],[ext])
        clean.magic()

    return render_template("index.html")

@app.route("/submit")
def submit():
    global arr
    return render_template("submit.html",path=arr[0],ext=arr[1],folder=arr[2])


if __name__ == "__main__":
    app.run(debug=True)