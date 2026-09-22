from typing import Literal

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field


class MediaCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    media_type: Literal["image", "audio", "video"]


class Media(MediaCreate):
    id: int


def create_app() -> FastAPI:
    app = FastAPI(title="多媒體目錄 API", version="1.0.0")
    media_items = {
        1: Media(id=1, title="校園活動照片", media_type="image"),
        2: Media(id=2, title="課程訪談錄音", media_type="audio"),
    }

    @app.get("/media", response_model=list[Media])
    def list_media(
        media_type: Literal["image", "audio", "video"] | None = Query(default=None),
    ) -> list[Media]:
        if media_type is None:
            return list(media_items.values())
        return [item for item in media_items.values() if item.media_type == media_type]

    @app.get("/media/{media_id}", response_model=Media)
    def read_media(media_id: int) -> Media:
        item = media_items.get(media_id)
        if item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="找不到媒體項目",
            )
        return item

    @app.post(
        "/media",
        response_model=Media,
        status_code=status.HTTP_201_CREATED,
    )
    def create_media(media: MediaCreate) -> Media:
        media_id = max(media_items, default=0) + 1
        item = Media(id=media_id, **media.model_dump())
        media_items[media_id] = item
        return item

    return app


app = create_app()
