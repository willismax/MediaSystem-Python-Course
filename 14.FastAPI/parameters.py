from fastapi import FastAPI, Query

app = FastAPI(title="FastAPI 參數範例")


@app.get("/media/{media_id}")
def read_media(
    media_id: int,
    media_type: str | None = Query(default=None, max_length=20),
) -> dict[str, int | str | None]:
    return {"media_id": media_id, "media_type": media_type}
