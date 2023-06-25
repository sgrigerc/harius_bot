import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declaretive
import sqlalchemy.orm as _orm


DATABASE_URL = "postgresql://harcy:32794@localhost/fastapi_database"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declaretive.declarative_base()

