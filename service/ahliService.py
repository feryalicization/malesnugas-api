from entity import db
import datetime
import json
from sqlalchemy import null, or_, and_, desc, table
import datetime

from entity.model import Ahli



def list_ahli():
    data = []
    query = db.session.query(Ahli).filter(Ahli.deleted_date == None)
    
    for x in query:
        data.append({
            "id": x.id,
            "full_name": x.full_name,
            "email": x.email,
            "created_by": x.created_by,
            "created_date": None if x.created_date == None else x.created_date.strftime("%Y-%m-%d"),
            "updated_date": None if x.updated_date == None else x.updated_date.strftime("%Y-%m-%d"),
        })

    return data




def Detail(id):
    data = []
    req = db.session.query(Ahli).filter(Ahli.deleted_date == None).filter(Ahli.id==id).first()
        
    if req:
        data = {
           "id": req.id,
            "full_name": req.full_name,
            "email": req.email,
            "created_by": req.created_by,
            "created_date": None if req.created_date == None else req.created_date.strftime("%Y-%m-%d"),
            "updated_date": None if req.updated_date == None else req.updated_date.strftime("%Y-%m-%d"),
            }

    return data

def Create(param, user_id):
    try:
        create = Ahli(
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
        req = db.session.query(Ahli).filter(Ahli.deleted_date == None).filter_by(id=id).first()
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
        req = db.session.query(Ahli).filter(Ahli.deleted_date == None).filter_by(id=id).first()
        if not req:
            return None

        req.deleted_date = datetime.datetime.now()
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False