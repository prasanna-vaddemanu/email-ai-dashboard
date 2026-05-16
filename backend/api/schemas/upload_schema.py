from pydantic import BaseModel


# =========================================================
# FILE UPLOAD RESPONSE
# =========================================================

class UploadResponse(BaseModel):

    filename: str

    message: str