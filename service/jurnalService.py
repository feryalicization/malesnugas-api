from entity import db
import datetime
import json
from sqlalchemy import null, or_, and_, desc, table
from datetime import datetime

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
            "user_id": x.user_id,
            "literature_id": x.literature_id,
            "created_date": None if x.created_date == None else x.created_date.strftime("%Y-%m-%d"),
            "update_date": None if x.update_date == None else x.update_date.strftime("%Y-%m-%d"),
        })

    return data