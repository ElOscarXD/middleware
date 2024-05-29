import json
from fastapi import FastAPI
import mariadb
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = mariadb.connect(
    user="Apiadmin",
    password="",
    host="192.168.100.92",
    port=3306,
    database="asteriskcdrdb"
)


@app.get("/")
async def Main():
    return RedirectResponse(url="/docs/")

@app.get("/get_registers")
async def get_registers_cdr():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cdr LIMIT 5000')
    reg = cursor.fetchall()
    res = []
    for i in reg:
        dict = {"id": str(i[0]),"Sucursal": i[8],"caller": i[3],"callee": i[2],"duration": i[9], "status": i[11]}
        res.append(dict)
    return {"llamadas": res}