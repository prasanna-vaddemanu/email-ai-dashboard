from fastapi.testclient import TestClient

from backend.api.main import app


# =========================================================
# TEST CLIENT
# =========================================================

client = TestClient(app)


# =========================================================
# TEST ROOT ENDPOINT
# =========================================================

def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {

        "message":
        "Email Threat Intelligence API Running"
    }


# =========================================================
# TEST HEALTH ENDPOINT
# =========================================================

def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


# =========================================================
# TEST PREDICT ENDPOINT
# =========================================================

def test_predict():

    payload = {

        "email_text":
        "FREE CASH now!!! Click here"
    }

    response = client.post(

        "/predict",

        json=payload
    )

    assert response.status_code == 200

    response_json = response.json()

    assert "prediction" in response_json

    assert "spam_probability" in response_json


# =========================================================
# TEST DRIFT ENDPOINT
# =========================================================

def test_drift_monitor():

    response = client.get(
        "/monitoring/drift"
    )

    assert response.status_code == 200