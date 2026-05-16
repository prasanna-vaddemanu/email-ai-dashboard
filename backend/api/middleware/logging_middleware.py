import time

from fastapi import Request

from backend.utils.logger import logger


# =========================================================
# LOGGING MIDDLEWARE
# =========================================================

async def log_requests(

    request: Request,

    call_next
):

    # ======================================
    # START TIMER
    # ======================================

    start_time = time.time()


    # ======================================
    # PROCESS REQUEST
    # ======================================

    response = await call_next(
        request
    )


    # ======================================
    # END TIMER
    # ======================================

    process_time = time.time() - start_time


    # ======================================
    # LOG MESSAGE
    # ======================================

    logger.info(

        f"{request.method} "

        f"{request.url.path} "

        f"Status={response.status_code} "

        f"Time={process_time:.4f}s"
    )


    return response