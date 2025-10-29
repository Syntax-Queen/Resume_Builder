import os
from app import app
from flask import flask, jsonify, send_file

@app.route('/create-resume', methods=['POST'])
def create_resume():
    