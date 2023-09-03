import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models import Base


@pytest.fixture(name="sqlite_session")
def sqlite_session_fixture() -> Session:
    # 建立 engine
    engine_url = "sqlite://"
    engine = create_engine(engine_url)

    # 建立資料表
    Base.metadata.create_all(engine)

    #  yield 出 Session
    with sessionmaker(bind=engine)() as session:
        yield session

    # 刪除資料表
    Base.metadata.drop_all(engine)