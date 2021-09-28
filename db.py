from sqlalchemy.engine import create_engine
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)


def startup(url='/:memory:'):

    engine = create_engine(f"sqlite+pysqlite://{url}", echo=True, future =True,convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                            autoflush=False,
                                            bind=engine))

    return db_session

