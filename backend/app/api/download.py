from fastapi import APIRouter

from app.models.request_models import DownloadRequest
from app.services.downloader import download_video

router = APIRouter(
    prefix="/download",
    tags=["Download"]
)

@router.post("/")
def download(request: DownloadRequest):
    return download_video(str(request.url))