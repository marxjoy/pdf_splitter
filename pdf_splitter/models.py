from flask_sqlalchemy import SQLAlchemy
from pdf_splitter import app

db = SQLAlchemy(app)


class DocumentContent(db.Model):
    '''
    Table contains one element of PDF document content.
    Element refers to document by document_id.
    Element got x,y coords and text.
    '''
    __tablename__ = 'documentcontent'
    id = db.Column('id', db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('documentpdf.id'),
                            nullable=True)
    x = db.Column('x', db.Float)
    y =  db.Column('y', db.Float)
    text =  db.Column('text', db.Text)


class DocumentPDF(db.Model):
    '''
    Parsed PDF Document model.
    '''
    __tablename__ = 'documentpdf'
    id = db.Column('id', db.Integer, primary_key=True)
    filename = db.Column('filename', db.Text)
    contents = db.relationship('DocumentContent', backref='documentpdf',
                               lazy=True)

    def __init__(self, filename, file_content):
        self.filename = filename
        db.session.add(self)
        db.session.commit()
        for content in file_content:
            x, y, text = content
            document_content = DocumentContent(document_id=self.id,
                                               x=x,
                                               y=y,
                                               text=text)
            db.session.add(document_content)
        db.session.commit()


db.create_all()