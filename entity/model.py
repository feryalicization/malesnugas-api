from . import db
from datetime import datetime



class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    is_metode = db.Column(db.Boolean())
    is_variabel = db.Column(db.Boolean())
    created_by = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)
    text = db.Column(db.Text)
    name = db.Column(db.String(225))
    updated_by = db.Column(db.Integer)



class Jurnal(db.Model):
    __tablename__ = "jurnal"
    id = db.Column(db.Integer, primary_key=True)
    is_metode = db.Column(db.Boolean())
    is_variabel = db.Column(db.Boolean())
    is_teori_penghubung = db.Column(db.Boolean())
    is_penelitian_terdahulu = db.Column(db.Boolean())
    text = db.Column(db.Text)
    name = db.Column(db.String(225))
    created_by = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer)


class Literature(db.Model):
    __tablename__ = "literature"
    id = db.Column(db.Integer, primary_key=True)
    is_jurnal = db.Column(db.Boolean())
    is_book = db.Column(db.Boolean())
    is_artikel = db.Column(db.Boolean())
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    ahli_id = db.Column(db.Integer)
    table_name = db.Column(db.Integer)
    table_id = db.Column(db.Integer)
    penerbit_id = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)



class Penerbit(db.Model):
    __tablename__ = "penerbit"
    id = db.Column(db.Integer, primary_key=True)
    is_book = db.Column(db.Boolean())
    is_jurnal = db.Column(db.Boolean())
    is_artikel = db.Column(db.Boolean())
    city = db.Column(db.String(225))
    jurnal_name = db.Column(db.String(225))
    penerbit_name = db.Column(db.String(225))
    year = db.Column(db.Integer)
    link = db.Column(db.String(225))
    issn = db.Column(db.String(225))
    nomor = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(225))
    password = db.Column(db.String(225))
    full_name = db.Column(db.String(225))
    email = db.Column(db.String(225))
    notelp = db.Column(db.String(225))
    gender = db.Column(db.Integer)
    universitas = db.Column(db.String(225))
    fakultas = db.Column(db.String(225))
    jurusan = db.Column(db.String(225))
    created_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)



class Ahli(db.Model):
    __tablename__ = "ahli"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(225))
    email = db.Column(db.String(225))
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)

    