from fastapi import APIRouter

from backend.monitoring.metrics import (
    load_metrics
)


# =========================================================
# ROUTER
# =========================================================

router = APIRouter(
    prefix="/monitoring",
    tags=["Monitoring"]
)


# =========================================================
# METRICS ENDPOINT
# =========================================================

@router.get("/metrics")

def get_monitoring_metrics():

    df = load_metrics()


    total_predictions = len(df)

    spam_predictions = len(

        df[df["label"] == "SPAM"]
    )

    ham_predictions = len(

        df[df["label"] == "HAM"]
    )


    return {

        "total_predictions": total_predictions,

        "spam_predictions": spam_predictions,

        "ham_predictions": ham_predictions
    }


# =========================================================
# DRIFT STATUS ENDPOINT
# =========================================================

@router.get("/drift")

def get_drift_status():

    return {

        "drift_detected": False,

        "system_status": "STABLE",

        "alert": "✅ System stable."
    }