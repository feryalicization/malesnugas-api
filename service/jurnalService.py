from entity import db
import datetime
import json
from sqlalchemy import null, or_, and_, desc, table
import datetime

from entity.model import Jurnal



def list_jurnal():
    data = []
    query = db.session.query(Jurnal).filter(Jurnal.deleted_date == None)
    
    for x in query:
        data.append({
            "id": x.id,
            "is_metode": x.is_metode,
            "is_variabel": x.is_variabel,
            "is_teori_penghubung": x.is_teori_penghubung,
            "is_penelitian_terdahulu": x.is_penelitian_terdahulu,
            "text": x.text,
            "penerbit_id": x.penerbit_id,
            "created_by": x.created_by,
            "literature_id": x.literature_id,
            "created_date": None if x.created_date == None else x.created_date.strftime("%Y-%m-%d"),
            "update_date": None if x.update_date == None else x.update_date.strftime("%Y-%m-%d"),
        })

    return data




def Detail(id):
    data = []
    req = db.session.query(Jurnal).filter(Jurnal.deleted_date == None).filter(Jurnal.id==id).first()
        
    if req:
        data = {
            "id": req.id,
            "is_metode": req.is_metode,
            "is_variabel": req.is_variabel,
            "is_teori_penghubung": req.is_teori_penghubung,
            "is_penelitian_terdahulu": req.is_penelitian_terdahulu,
            "text": req.text,
            "penerbit_id": req.penerbit_id,
            "created_by": req.created_by,
            "literature_id": req.literature_id,
            "created_date": None if req.created_date == None else req.created_date.strftime("%Y-%m-%d"),
            "update_date": None if req.update_date == None else req.update_date.strftime("%Y-%m-%d"),
            }

    return data

def Create(param, user_id):
    try:
        create = Jurnal(
            is_metode=param['is_metode'],
            is_variabel=param['is_variabel'],
            is_teori_penghubung=param['is_teori_penghubung'],
            is_penelitian_terdahulu=param['is_penelitian_terdahulu'],
            text=param['text'],
            penerbit_id=param['penerbit_id'],
            literature_id=param['literature_id'],
   
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
        req = db.session.query(Jurnal).filter(Jurnal.deleted_date == None).filter_by(id=id).first()
        if not req:
            return None

        req.is_metode=param['is_metode']
        req.is_variabel=param['is_variabel']
        req.is_teori_penghubung=param['is_teori_penghubung']
        req.is_penelitian_terdahulu=param['is_penelitian_terdahulu']
        req.text=param['text'],
        req.penerbit_id=param['penerbit_id'],
        req.literature_id=param['literature_id'],

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
        req = db.session.query(Jurnal).filter(Jurnal.deleted_date == None).filter_by(id=id).first()
        if not req:
            return None

        req.deleted_date = datetime.datetime.now()
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False