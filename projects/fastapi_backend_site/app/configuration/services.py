from app.pkg.postgres_tools.tools import DATABASE_URL, engine, SessionLocal, Base as _DATABASE_URL, _engine, _SessionLocal, _Base
from app.pkg.postgres_tools.models import Contact as _Contact


def _add_tables():

   return _Base.metadata.create_all(bind=_engine)
