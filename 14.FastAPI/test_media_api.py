import pytest
from fastapi.testclient import TestClient

from media_api import create_app


@pytest.fixture
def client() -> TestClient:
    return TestClient(create_app())


def test_lists_media(client: TestClient) -> None:
    response = client.get("/media")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "校園活動照片", "media_type": "image"},
        {"id": 2, "title": "課程訪談錄音", "media_type": "audio"},
    ]


def test_filters_media_by_type(client: TestClient) -> None:
    response = client.get("/media", params={"media_type": "audio"})

    assert response.status_code == 200
    assert response.json() == [
        {"id": 2, "title": "課程訪談錄音", "media_type": "audio"}
    ]


def test_creates_media(client: TestClient) -> None:
    response = client.post(
        "/media",
        json={"title": "期末成果影片", "media_type": "video"},
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 3,
        "title": "期末成果影片",
        "media_type": "video",
    }


def test_returns_not_found_for_unknown_media(client: TestClient) -> None:
    response = client.get("/media/99")

    assert response.status_code == 404
    assert response.json() == {"detail": "找不到媒體項目"}


def test_validates_media_input(client: TestClient) -> None:
    response = client.post(
        "/media",
        json={"title": "", "media_type": "text"},
    )

    assert response.status_code == 422
