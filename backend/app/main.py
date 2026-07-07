from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.download import router as download_router
from app.api.clip import router as clip_router

app = FastAPI(title="YouTube Clip Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(download_router, prefix="/api")
app.include_router(clip_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "API is running"}