from flask import Flask, request, json, jsonify, abort
from flask_restful import Api, Resource
import os
import config
import webbrowser
import pyautogui
app = Flask(__name__)

@app.route('/api/command/<string:command>', methods=['GET'])
def command(command):
    username = request.args.get("username")
    password = request.args.get("password")
    if username == config.username and password == config.password:
        command = command.replace("%", " ")
        command = command.replace("1", "/")
        command = command.replace("2", "\\")
        os.system(command)
        return "200"
    else:
        abort(404)

@app.route('/api/apps/<string:explorer_path>', methods=['GET'])
def apps(explorer_path):
    username = request.args.get("username")
    password = request.args.get("password")
    if username == config.username and password == config.password:
        explorer_path = explorer_path.replace("%", " ")
        explorer_path = explorer_path.replace("1", "/")
        explorer_path = explorer_path.replace("2", "\\")
        explorer_path = explorer_path.replace("3", ".")
        os.startfile(explorer_path)
        return "200"
    else:
        return abort(403)

@app.route('/api/browser/<string:browser>', methods=['GET'])
def browser(browser):
    username = request.args.get("username")
    password = request.args.get("password")
    if username == config.username and password == config.password:
        browser = browser.replace("%", " ")
        browser = browser.replace("1", "/")
        browser = browser.replace("2", "\\")
        browser = browser.replace("3", ".")
        webbrowser.open(browser)
        return "200"
    else:
        return abort(403)

@app.route('/api/hotkeys/<string:hotkey>', methods=['GET'])
def hotkey(hotkey):
    username = request.args.get("username")
    password = request.args.get("password")
    if username == config.username and password == config.password:
        if "+" in hotkey:
            hotkey = hotkey.split("+")
            if len(hotkey) == 2:
                pyautogui.hotkey(hotkey[0], hotkey[1])
            elif len(hotkey) == 3:
                pyautogui.hotkey(hotkey[0], hotkey[1], hotkey[2])
            else:
                abort(404)
        else:
            pyautogui.hotkey(hotkey)
        return "200"
    else:
        return abort(403)
if __name__ == '__app__':
    app.run()