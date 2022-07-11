import os

from flask import session, redirect, url_for, render_template, request, send_from_directory, current_app
from . import main
from tolino.ebooks import get_epubs, read_info

@main.route('/')
def index():
    epubs = get_epubs(current_app.config["library_path"])

    page = request.args.get('page')
    if page is None:
        page = 1

    page = int(page)

    if page <= 0:
        page = 1

    num_ebooks = 6
    start_offset = (page - 1) * num_ebooks

    epubs = epubs[start_offset:start_offset + num_ebooks]

    ebooks = [ read_info(epub) for epub in epubs ]

    return render_template('index.html', ebooks=ebooks, page=page)

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