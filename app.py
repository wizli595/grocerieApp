import copy
from flask import Flask, render_template, url_for, request, session
import sqlite3
import random

app = Flask(__name__)
app.secret_key = "secret"

# first page or the main


@app.route('/', methods=["POST", "GET"])
def index():
    # start using session for (change LOCAL to GLOBAL)
    session["all_items"], session["shopping"] = getData()
    return render_template("index.html", title="page", datas=session["all_items"], needs=session["shopping"])

# how we add th item to the list


@app.route("/add_item", methods=["post"])
def add_items():
    session["shopping"].append(request.form["select_item"])
    # edit for not just add one item
    session.modified = True
    return render_template("index.html", title="page", datas=session["all_items"], needs=session["shopping"])

# how we remove


@app.route("/remove_items", methods=["post"])
def remove_items():
    checked = request.form.getlist("check")
    # looping into all boxes
    for item in checked:
        if item in session["shopping"]:
            idx = session["shopping"].index(item)
            session["shopping"].pop(idx)
            session.modified = True

    return render_template("index.html", datas=session["all_items"],
                           needs=session["shopping"])

# fetching the data from the table


def getData():
    db = sqlite3.connect('grocery_list.db')
    Cursor = db.cursor()
    Cursor.execute("select * from groceries")
    all_data = Cursor.fetchall()
    all_data = [str(val[1]) for val in all_data]
    # using random for just a start
    shopping = copy.deepcopy(all_data)
    random.shuffle(shopping)
    shopping = shopping[0:7]
    return all_data, shopping


if __name__ == "__main__":
    app.run(debug=True)
