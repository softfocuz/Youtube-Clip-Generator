from fastapi import APIRouter

router = APIRouter(tags=["Clip"])

@router.post("/clip")
def clip_video():
    return {
        "message": "Clip endpoint working"
    }