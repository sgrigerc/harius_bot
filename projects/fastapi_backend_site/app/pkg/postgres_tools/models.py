import datetime as _dt
import sqlalchemy as _sql

import tools as _tools

class Contact(_tools.Base):

   __tablename = "contacts"
   id = _sql.Column(_sql.Integer, primary_key=True, index=True)
   first_name = _sql.Column(_sql.String, index=True)
   lust_name = _sql.Column(_sql.String, index=True)
   email = _sql.Column(_sql.String, index=True, unique=True)
   phone_number= _sql.Column(_sql.String, index=True, unique=True)
   date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow) 



