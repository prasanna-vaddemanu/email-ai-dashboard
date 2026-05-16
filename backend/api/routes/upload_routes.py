from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from backend.api.schemas.upload_schema import (
    UploadResponse
)


# =========================================================
# ROUTER
# =========================================================

router = APIRouter()


# =========================================================
# FILE UPLOAD ENDPOINT
# =========================================================

@router.post(
    "/upload",
    response_model=UploadResponse
)

async def upload_email_file(

    file: UploadFile = File(...)
):

    return {

        "filename": file.filename,

        "message": "File uploaded successfully"
    }