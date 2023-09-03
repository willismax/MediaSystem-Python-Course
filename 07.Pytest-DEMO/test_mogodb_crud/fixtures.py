import pytest
from mongomock.mongo_client import MongoClient


@pytest.fixture(name="conn")
def mongo_client_fixture() -> MongoClient:
    with MongoClient() as conn:
        yield conn