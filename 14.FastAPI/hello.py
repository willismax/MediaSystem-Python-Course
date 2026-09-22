from fastapi import FastAPI

app = FastAPI(title="FastAPI 第一支 API")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, FastAPI!"}
