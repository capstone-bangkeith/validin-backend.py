from fastapi import FastAPI

from db_sqlite import Database

app = FastAPI()

db = Database()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/kode-wilayah")
async def kode_wilayah(kode: str | None = None):
    return {"result": db.get_kode_wilayah(kode)}


@app.get("/kode-wilayah/{kode}")
async def kode_wilayah_path(kode: str | None = None):
    return {"result": db.get_kode_wilayah(kode)}
