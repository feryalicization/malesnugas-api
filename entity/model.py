from . import db
from datetime import datetime



class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    is_metode = db.Column(db.Boolean())
    is_variabel = db.Column(db.Boolean())
    user_id = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)
    text = db.Column(db.Text)
    penerbit_id = db.Column(db.Integer)
    literature_id = db.Column(db.Integer)



class Jurnal(db.Model):
    __tablename__ = "jurnal"
    id = db.Column(db.Integer, primary_key=True)
    is_metode = db.Column(db.Boolean())
    is_variabel = db.Column(db.Boolean())
    is_teori_penghubung = db.Column(db.Boolean())
    is_penelitian_terdahulu = db.Column(db.Boolean())
    text = db.Column(db.Text)
    penerbit_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)
    literature_id = db.Column(db.Integer)


class Literature(db.Model):
    __tablename__ = "literature"
    id = db.Column(db.Integer, primary_key=True)
    is_jurnal = db.Column(db.Boolean())
    is_book = db.Column(db.Boolean())
    is_artikel = db.Column(db.Boolean())
    user_id = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)



class Penerbit(db.Model):
    __tablename__ = "penerbit"
    id = db.Column(db.Integer, primary_key=True)
    is_book = db.Column(db.Boolean())
    is_jurnal = db.Column(db.Boolean())
    is_artikel = db.Column(db.Boolean())
    name = db.Column(db.String(225))
    city = db.Column(db.String(225))
    jurnal_name = db.Column(db.String(225))
    penerbit_name = db.Column(db.String(225))
    year = db.Column(db.DateTime)
    link = db.Column(db.String(225))
    issn = db.Column(db.String(225))
    user_id = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)

