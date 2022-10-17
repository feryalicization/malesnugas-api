from entity import db
import datetime
import json
from sqlalchemy import null, or_, and_, desc, table
import datetime

from entity.model import Penerbit, User



def list_penerbit():
    data = []
    query = db.session.query(Penerbit).filter(Penerbit.deleted_date == None)
    
    for x in query:
        user = db.session.query(User).filter(User.id == x.created_by).first()
        data.append({
            "id": x.id,
            "is_book": x.is_book,
            "is_jurnal": x.is_jurnal,
            "is_artikel": x.is_artikel,
            "name": x.name,
            "city": x.city,
            "jurnal_name": x.jurnal_name,
            "penerbit_name": x.penerbit_name,
            "year": x.year,
            "link": x.link,
            "issn": x.issn,
            "created_by": user.full_name,
            "created_date": None if x.created_date == None else x.created_date.strftime("%Y-%m-%d"),
            "updated_date": None if x.updated_date == None else x.updated_date.strftime("%Y-%m-%d"),
        })

    return data




def Detail(id):
    data = []
    req = db.session.query(Penerbit).filter(Penerbit.deleted_date == None).filter(Penerbit.id==id).first()
        
    if req:
        created = db.session.query(User).filter(User.id == req.created_by).first()
        update = db.session.query(User.full_name.label('updated_by')).join(
                Penerbit, Penerbit.updated_by == User.id).filter(User.id == req.updated_by).first()
        data = {
            "id": req.id,
            "is_book": req.is_book,
            "is_jurnal": req.is_jurnal,
            "is_artikel": req.is_artikel,
            "name": req.name,
            "city": req.city,
            "jurnal_name": req.jurnal_name,
            "penerbit_name": req.penerbit_name,
            "year": req.year,
            "link": req.link,
            "issn": req.issn,
            "created_by": None if created.full_name == None else created.full_name,
            "updated_by": None if req.updated_by == None else update.updated_by,
            "created_date": None if req.created_date == None else req.created_date.strftime("%Y-%m-%d"),
            "updated_date": None if req.updated_date == None else req.updated_date.strftime("%Y-%m-%d"),
            }

    return data

def Create(param, user_id):
    try:
        create = Penerbit(
            is_book=param['is_book'],
            is_jurnal=param['is_jurnal'],
            is_artikel=param['is_artikel'],
            name=param['name'],
            city=param['city'],
            jurnal_name=param['jurnal_name'],
            penerbit_name=param['penerbit_name'],
            year=param['year'],
            link=param['link'],
            issn=param['issn'],
   
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
        req = db.session.query(Penerbit).filter(Penerbit.deleted_date == None).filter_by(id=id).first()
        if not req:
            return None

        req.is_book=param['is_book']
        req.is_jurnal=param['is_jurnal']
        req.is_artikel=param['is_artikel']
        req.name=param['name'],
        req.city=param['city'],
        req.jurnal_name=param['jurnal_name'],
        req.penerbit_name=param['penerbit_name'],
        req.year=param['year'],
        req.link=param['link'],
        req.issn=param['issn'],

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
        req = db.session.query(Penerbit).filter(Penerbit.deleted_date == None).filter_by(id=id).first()
        if not req:
            return None

        req.deleted_date = datetime.datetime.now()
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False