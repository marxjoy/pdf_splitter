from flask import Flask
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'db_file.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 't%$#&*DFDKKJDF$)D848*C#g'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.debug = True


from pdf_splitter import models
from pdf_splitter import views