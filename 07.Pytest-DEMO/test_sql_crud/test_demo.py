from crud import create_user_in_sqlite
from models import User
from fixtures import sqlite_session_fixture
from sqlalchemy.orm import Session
from datetime import datetime

use_fixtures = [sqlite_session_fixture]


def test_create_user_in_sqlite(sqlite_session: Session):
    data = User(username="test_user", birthday=datetime.now())

    result: User = create_user_in_sqlite(data=data, session=sqlite_session)
    print(result.__dict__)

    assert result.username == data.username