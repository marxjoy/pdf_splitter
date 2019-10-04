from flask import flash
from flask import redirect, render_template, request, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from pdf_splitter import app
from pdf_splitter.models import DocumentPDF, DocumentContent
from pdf_splitter.models import db
from pdf_splitter.pdf_parser import allowed_file, pdfparser

import os
from werkzeug.utils import secure_filename

admin = Admin(app)
admin.add_view(ModelView(DocumentPDF, db.session))


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            page_content = pdfparser(file_path)
            document = DocumentPDF(filename=filename)
            db.session.add(document)
            db.session.commit()
            for content in page_content:
                x, y, text = content
                document_content = DocumentContent(document_id=document.id,
                                                   x=x,
                                                   y=y,
                                                   text=text)
                db.session.add(document_content)
            db.session.commit()
            return redirect(url_for('parsed_file',
                                    file_id=document.id))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/parsed/<file_id>')
def parsed_file(file_id):
    file = DocumentPDF.query.filter_by(id=file_id).first()
    contents = DocumentContent.query.filter_by(document_id=file.id)
    return render_template("example.html", file=file, contents=contents)
