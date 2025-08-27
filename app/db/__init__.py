from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.utils.fs_util import DEFAULT_PATH

engine = create_engine(url=f'sqlite:///{DEFAULT_PATH}/app.db', echo=True)
session_maker = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = session_maker()