import os

from flask import session, redirect, url_for, render_template, request, send_from_directory
from . import main

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/dataset/<string:file>')
def get_dataset(file):
    print(file)
    filename = None
    
    if file == "works":
        filename = "works.csv"
    elif file == "authors":
        filename = "authors.csv"
    elif file == "manuscripts":
        filename = "manuscripts.csv"
    elif file == "customs":
        filename = "customs.csv"
    
    if filename is not None:
        return send_from_directory("../", filename, max_age=0)
    else:
        return "miep"