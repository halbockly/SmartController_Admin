# -*- coding: utf-8 -*-
import json
import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

BASE_DIR = os.path.abspath('/')
DATA_DIR = os.path.join(BASE_DIR, "home/pi/")

@app.route('/')
def index():
    return render_template('Admin/Home.html')


@app.route('/Kaden')
def buttons():
    with open(DATA_DIR + "kaden.json", "r", encoding='utf8') as f:
        data = json.load(f)
    return render_template('Admin/Kaden.html', data=data)


@app.route('/saveKaden', methods=["POST"])
def save_button():
    name = request.form['name']
    status = request.form["status"]
    id = request.form["id"]

    path = DATA_DIR + "kaden.json"
    with open(path, "r", encoding='utf8') as f:
        data = json.load(f)
        data[id]["name"] = name
        data[id]["status"] = status
        with open(path, 'w', encoding='utf8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
    return redirect("/Kaden")


if __name__ == "__main__":
    app.run()
