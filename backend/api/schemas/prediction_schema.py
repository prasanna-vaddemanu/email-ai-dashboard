from pydantic import BaseModel


# =========================================================
# EMAIL PREDICTION REQUEST
# =========================================================

class EmailRequest(BaseModel):

    email_text: str