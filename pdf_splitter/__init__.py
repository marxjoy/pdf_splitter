from flask import Flask
import os


UPLOAD_FOLDER = 'uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'db_file.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 't%$#&*DFDKKJDF$)D848*C#g'


#app.config.from_object(__name__)

from pdf_splitter import models
from pdf_splitter import views
from pdf_splitter import pdf_parser
