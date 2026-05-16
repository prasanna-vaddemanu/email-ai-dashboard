from fastapi import APIRouter

from backend.api.schemas.prediction_schema import (
    EmailRequest
)

from backend.core.prediction import (
    predict_email
)

from backend.core.threat_scoring import (
    calculate_risk_score
)

from backend.monitoring.metrics import (
    log_prediction
)


# =========================================================
# ROUTER
# =========================================================

router = APIRouter()


# =========================================================
# PREDICTION ENDPOINT
# =========================================================

@router.post("/predict")

def predict(request: EmailRequest):

    # =====================================================
    # EMAIL CONTENT
    # =====================================================

    email_text = request.email_text


    # =====================================================
    # ML PREDICTION
    # =====================================================

    prediction_result = predict_email(
        email_text
    )


    # =====================================================
    # THREAT INTELLIGENCE
    # =====================================================

    threat_result = calculate_risk_score(
        email_text
    )


    # =====================================================
    # VALUES
    # =====================================================

    spam_probability = prediction_result[
        "spam_probability"
    ]

    risk_score = threat_result[
        "risk_score"
    ]


    # =====================================================
    # HYBRID SECURITY DECISION ENGINE
    # =====================================================

    # ---------------------------------------------
    # HIGH RISK OVERRIDE
    # ---------------------------------------------

    if risk_score >= 50:

        final_prediction = 1

        final_label = "SPAM"


    # ---------------------------------------------
    # STRONG ML + MODERATE RISK
    # ---------------------------------------------

    elif (

        spam_probability >= 0.70

        and

        risk_score >= 20
    ):

        final_prediction = 1

        final_label = "SPAM"


    # ---------------------------------------------
    # VERY HIGH ML CONFIDENCE
    # ---------------------------------------------

    elif spam_probability >= 0.95:

        final_prediction = 1

        final_label = "SPAM"


    # ---------------------------------------------
    # SAFE EMAIL
    # ---------------------------------------------

    else:

        final_prediction = 0

        final_label = "HAM"


    # =====================================================
    # LOG PREDICTION
    # =====================================================

    log_prediction(

        prediction=final_prediction,

        label=final_label,

        spam_probability=round(
            spam_probability,
            4
        ),

        risk_score=risk_score,

        threat_level=threat_result[
            "threat_level"
        ]
    )


    # =====================================================
    # FINAL RESPONSE
    # =====================================================

    return {

        "prediction": final_prediction,

        "label": final_label,

        "spam_probability": round(
            spam_probability,
            4
        ),

        "clean_text": prediction_result[
            "clean_text"
        ],

        "risk_score": risk_score,

        "threat_level": threat_result[
            "threat_level"
        ],

        "reasons": threat_result[
            "reasons"
        ],

        "score_breakdown": threat_result[
            "score_breakdown"
        ],

        "detected_patterns": threat_result[
            "detected_patterns"
        ],

        "url_count": threat_result[
            "url_count"
        ],

        "html_tag_count": threat_result[
            "html_tag_count"
        ],

        "uppercase_ratio": threat_result[
            "uppercase_ratio"
        ],

        "exclamation_count": threat_result[
            "exclamation_count"
        ]
    }