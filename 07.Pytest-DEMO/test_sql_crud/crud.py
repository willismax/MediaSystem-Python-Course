from sqlalchemy.orm import Session
from models import User


def create_user_in_sqlite(data: User, session: Session) -> User:
    session.add(data)
    session.commit()
    session.refresh(data)

    return data