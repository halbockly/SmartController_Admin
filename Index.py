# -*- coding: utf-8 -*-
import json
import os
from bottle import TEMPLATE_PATH, jinja2_template as template
from bottle import run, route, static_file

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/views")


@route('/static/<_dir>/<_filename>')
def server_static(_dir, _filename):
    return static_file(_filename, root='./static/' + _dir + '/')


@route('/')
def index():
    return template('views/Admin/Home')


@route('/Buttons')
def buttons():
    with open("data/buttons.json", "r") as f:
        data = json.load(f)
    return template('views/Admin/Buttons', data=data)


@route('/Status')
def status():
    with open("data/status.json", "r") as f:
        data = json.load(f)
    return template('views/Admin/Status', data=data)


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True, reloader=True)
