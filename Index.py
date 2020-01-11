# -*- coding: utf-8 -*-
import json
import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# from bottle import TEMPLATE_PATH, jinja2_template as template, redirect
# from bottle import run, route, static_file, request

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
# TEMPLATE_PATH.append(BASE_DIR + "/views")

#
# @route('/static/<_dir>/<_filename>')
# def server_static(_dir, _filename):
#     return static_file(_filename, root='./static/' + _dir + '/')


@app.route('/')
def index():
    return render_template('Admin/Home.html')


@app.route('/Kaden')
def buttons():
    with open("data/kaden.json", "r", encoding='utf8') as f:
        data = json.load(f)
    return render_template('Admin/Kaden.html', data=data)

@app.route('/saveKaden', methods=["POST"])
def save_button():
    name = request.form['name']
    status = request.form["status"]
    id = request.form["id"]

    path = "data/kaden.json"
    with open(path, "r", encoding='utf8') as f:
        data = json.load(f)
        data[id]["name"] = name
        data[id]["status"] = status
        with open(path, 'w', encoding='utf8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
    return redirect("/Kaden")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
