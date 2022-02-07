from flask import Flask, jsonify
from task_manager import command_datasource

app = Flask(__name__)

@app.route('/commands')
def commands():
    data = command_datasource.findall()
    return jsonify(data)