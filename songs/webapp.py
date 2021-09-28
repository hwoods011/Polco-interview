from . import app   
from . import routes  # For import side-effects of setting up routes.

from . import db

db.init_db()