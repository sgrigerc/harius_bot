import models as _models
import tools as _tools


def _add_tables():

   return _tools.Base.metadata.create_all(bind=_tools.engine)
