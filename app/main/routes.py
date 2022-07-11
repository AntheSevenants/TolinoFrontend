import os
import base64

from flask import session, redirect, url_for, render_template, request, send_file, current_app
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

    return render_template('index.html', ebooks=ebooks, page=page, start_offset=start_offset)

@main.route('/epub/<int:epub_index>.epub')
def get_dataset(epub_index):
    epubs = get_epubs(current_app.config["library_path"])

    if epub_index > len(epubs):
        return

    epub = epubs[epub_index]
    
    return send_file(epub.resolve(), max_age=0)