import os


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = os.path.abspath(

    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)


# =========================================================
# DATA DIRECTORIES
# =========================================================

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

RAW_DATA_DIR = os.path.join(
    DATA_DIR,
    "raw"
)

PROCESSED_DATA_DIR = os.path.join(
    DATA_DIR,
    "processed"
)


# =========================================================
# MODEL DIRECTORY
# =========================================================

MODELS_DIR = os.path.join(
    BASE_DIR,
    "models",
    "production"
)


# =========================================================
# LOG DIRECTORY
# =========================================================

LOGS_DIR = os.path.join(
    BASE_DIR,
    "logs"
)