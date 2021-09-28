import sqlite3
from flask import current_app, g
from . import app

def get_db():
    with app.app_context():
        if 'db' not in g:
            g.db = sqlite3.connect(
                'dev.db',
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row

        return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():

    db = get_db()

    
    with app.app_context():
        with open('schema.sql') as f:
            data = f.read()
            db.executescript(data)
        
        with open('seed.sql') as f:
            seeds = f.read()
            db.executescript(seeds)