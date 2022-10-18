from entity import db
import datetime
import json
from sqlalchemy import null, or_, and_, desc, table
import datetime

from entity.model import Literature, User, Ahli, Book, Jurnal, Penerbit
from sqlalchemy.orm import aliased


def list_literature():
    data = []

    query = db.session.query(Literature.id, Literature.is_jurnal,
    Literature.is_book, Literature.is_artikel,
    Ahli.full_name,
    Book.name.label('book'), 
    Book.text.label('book_text'),
    Jurnal.name.label('jurnal'),
    Jurnal.text.label('jurnal_text'),
    Penerbit.year
    )\
    .join(Book, and_(Literature.table_id == Book.id, Literature.table_name == 'book'), isouter=True)\
    .join(Jurnal, and_(Literature.table_id == Jurnal.id, Literature.table_name == 'jurnal'), isouter=True)\
    .join(Penerbit, Penerbit.id == Literature.penerbit_id, isouter=True)\
    .join(Ahli, Ahli.id == Literature.ahli_id)\
    .filter(Literature.deleted_date == None)
    
    
    for x in query:

        data.append({
            "id": x.id,
            "ahli": x.full_name, 
            "tahun": x.year,
            "judul": x.jurnal if x.is_jurnal == True or x.is_book == False or x.is_book == None else x.book,
            "tipe": "jurnal" if x.is_jurnal == True or x.is_book == False or x.is_book == None else "book",
        })

    return data




def Detail(id):
    data = []
    req = db.session.query(Literature.id, Literature.is_jurnal,
    Literature.is_book, Literature.is_artikel,
    Ahli.full_name,
    Book.name.label('book'), 
    Book.text.label('book_text'),
    Book.is_metode.label("book_is_metode"), Book.is_variabel.label("book_is_variabel"),
    Jurnal.name.label('jurnal'),
    Jurnal.text.label('jurnal_text'),
    Jurnal.is_metode.label('jurnal_is_metode'),
    Jurnal.is_variabel.label("jurnal_is_variabel"), Jurnal.is_teori_penghubung.label('jurnal_is_teori_penghubung'),
    Jurnal.is_penelitian_terdahulu.label('jurnal_is_penelitian_terdahulu'),
    Penerbit.year,
    Penerbit.is_jurnal.label('penerbit_is_jurnal'), Penerbit.is_book.label('penerbit_is_book'),
    Penerbit.jurnal_name,
    Penerbit.penerbit_name,
    Penerbit.issn,
    Penerbit.nomor,
    Penerbit.volume,
    Penerbit.city,
    Penerbit.link,
    Literature.created_by,
    Literature.updated_by,
    Literature.created_date,
    Literature.updated_date
    )\
    .join(Book, and_(Literature.table_id == Book.id, Literature.table_name == 'book'), isouter=True)\
    .join(Jurnal, and_(Literature.table_id == Jurnal.id, Literature.table_name == 'jurnal'), isouter=True)\
    .join(Penerbit, Penerbit.id == Literature.penerbit_id, isouter=True)\
    .join(Ahli, Ahli.id == Literature.ahli_id)\
    .filter(Literature.deleted_date == None).filter(Literature.id==id).first()
        
    if req:

        created = db.session.query(User).filter(User.id == req.created_by).first()

        update = db.session.query(User.full_name.label('updated_by')).join(
                Literature, Literature.updated_by == User.id).filter(User.id == req.updated_by).first()

        if req.penerbit_is_jurnal == True:
            ref = req.jurnal_name
            dafpus = f"{req.full_name}. ({req.year}). {req.jurnal}. {req.jurnal_name}, Vol. {req.volume}, No. {req.nomor}, ISSN:{req.issn}, sumber: {req.link}"
            
            if req.jurnal_is_metode == True:
                jenis = "metode"
            elif req.jurnal_is_variabel == True:
                jenis = "variabel"
            elif req.jurnal_is_teori_penghubung == True:
                jenis = "teori penghubung"
            elif req.jurnal_is_penelitian_terdahulu == True:
                jenis = "penelitian terdahulu"
            else:
                None
            
        elif req.penerbit_is_book == True:
            ref = req.penerbit_name
            dafpus = f"{req.full_name}. ({req.year}). {req.book}. {req.city}: {req.penerbit_name}, ISSN:{req.issn}."

            if req.book_is_metode == True:
                jenis = "metode"
            elif req.book_is_variabel == True:
                jenis = "variabel"
            else:
                None

        else:
            "is artikel"

        data = {
            "id": req.id,
            "ahli": req.full_name, 
            "tahun": req.year,
            "judul": req.jurnal if req.is_jurnal == True or req.is_book == False or req.is_book == None else req.book,
            "tipe": "jurnal" if req.is_jurnal == True or req.is_book == False or req.is_book == None  else "book",
            "literature": req.jurnal_text if req.is_jurnal == True or req.is_book == False or req.is_book == None else req.book_text,
            "penerbit": ref,
            "jenis": jenis,
            "daftar_pustaka": dafpus,
            "created_by": created.full_name,
            "updated_by": None if req.updated_by == None else update.updated_by,
            "created_date": None if req.created_date == None else req.created_date.strftime("%Y-%m-%d"),
            "updated_date": None if req.updated_date == None else req.updated_date.strftime("%Y-%m-%d"),
            }

    return data

def Create(param, user_id):
    try:
        create = Literature(
            full_name=param['full_name'],
            email=param['email'],
   
            #Generate
            created_date=datetime.datetime.now(),
            created_by=user_id,
        )

        db.session.add(create)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
        return False

def Edit(id, param, user_id):
    try:
        req = db.session.query(Literature).filter(Literature.deleted_date == None).filter_by(id=id).first()
        if not req:
            return None

        req.full_name=param['full_name'],
        req.email=param['email'],

        #Generate
        req.updated_date=datetime.datetime.now(),
        req.updated_by=user_id,

        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(e)
        return False

def Delete(id):
    try:
        req = db.session.query(Literature).filter(Literature.deleted_date == None).filter_by(id=id).first()
        if not req:
            return None

        req.deleted_date = datetime.datetime.now()
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False