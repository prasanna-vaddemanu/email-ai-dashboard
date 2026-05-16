from fastapi import FastAPI

from backend.api.routes.prediction_routes import (
    router as prediction_router
)

from backend.api.routes.upload_routes import (
    router as upload_router
)

from backend.api.routes.monitoring_routes import (
    router as monitoring_router
)

from backend.api.middleware.logging_middleware import (
    log_requests
)


# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(

    title="Email Threat Intelligence API",

    description="AI-powered spam and phishing detection API",

    version="1.0.0"
)


# =========================================================
# REGISTER MIDDLEWARE
# =========================================================

app.middleware("http")(

    log_requests
)


# =========================================================
# ROOT ENDPOINT
# =========================================================

@app.get("/")

def home():

    return {

        "message": "Email Threat Intelligence API Running"
    }


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")

def health_check():

    return {

        "status": "healthy"
    }


# =========================================================
# REGISTER ROUTES
# =========================================================

app.include_router(

    prediction_router
)

app.include_router(

    upload_router
)

app.include_router(

    monitoring_router
)