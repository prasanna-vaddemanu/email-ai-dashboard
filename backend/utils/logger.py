import logging
import os

from backend.utils.config import LOGS_DIR


# =========================================================
# CREATE LOG DIRECTORY
# =========================================================

os.makedirs(
    LOGS_DIR,
    exist_ok=True
)


# =========================================================
# LOGGER CONFIG
# =========================================================

logging.basicConfig(

    filename=os.path.join(
        LOGS_DIR,
        "backend.log"
    ),

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"
)


# =========================================================
# LOGGER
# =========================================================

logger = logging.getLogger(
    "email_threat_intelligence"
)