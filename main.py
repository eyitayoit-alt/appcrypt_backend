import pathlib
import os
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from .utils import decrypt, encrypt

origins = [
    "http://localhost:1234",
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/encodefile")
async def encodefile(request: Request):
    form = await request.form()
    file = form["file"]
    type = form["type"]
    ext_type = [".jpeg", ".pdf", ".txt", ".png", ".doc"]
    file_ext = pathlib.Path(file.filename).suffix
    if file_ext in ext_type:
        if type == "Encrypt":
            try:
                filepath, keypath = await encrypt(file)
                return {"filepath": filepath.strip("."), "keypath": keypath.strip(".")}
            except Exception as err:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=err)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="File type not supported"
        )


@app.post("/decodefile")
async def decodefile(request: Request):
    form = await request.form()
    file = form["file"]
    keyfile = form["keyfile"]
    type = form["type"]
    file_ext = pathlib.Path(keyfile.filename).suffix
    if file_ext == ".key":
        if type == "Decrypt":
            try:
                filepath = await decrypt(file, keyfile)
                return {"filepath": filepath.strip(".")}
            except Exception as err:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=err)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Key type not supported"
        )


@app.get("/download/{file_path:path}")
async def download(file_path: str):
    requestPath = file_path
    if os.path.exists(requestPath):
        return FileResponse(requestPath, media_type="application/octet-stream")
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="File does not exist"
        )
