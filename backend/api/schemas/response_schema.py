from pydantic import BaseModel

from typing import List


# =========================================================
# PREDICTION RESPONSE
# =========================================================

class PredictionResponse(BaseModel):

    prediction: int

    spam_probability: float

    clean_text: str

    risk_score: int

    threat_level: str

    reasons: List[str]