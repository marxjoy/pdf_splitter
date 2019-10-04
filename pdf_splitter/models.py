from flask_sqlalchemy import SQLAlchemy
from pdf_splitter import app


db = SQLAlchemy(app)


class DocumentPDF(db.Model):
    __tablename__ = 'documentpdf'
    id = db.Column('id', db.Integer, primary_key=True)
    filename = db.Column('filename', db.Text)
    contents = db.relationship('DocumentContent', backref='documentpdf',
                               lazy=True)


class DocumentContent(db.Model):
    __tablename__ = 'documentcontent'
    id = db.Column('id', db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('documentpdf.id'),
                            nullable=True)
    x = db.Column('x', db.Float)
    y =  db.Column('y', db.Float)
    text =  db.Column('text', db.Text)


db.create_all()