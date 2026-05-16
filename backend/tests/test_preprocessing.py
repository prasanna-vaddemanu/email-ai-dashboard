from backend.core.preprocessing import (
    preprocess_text
)


# =========================================================
# TEST PREPROCESSING
# =========================================================

def test_preprocess_text():

    sample_email = """

    CONGRATULATIONS!!!

    You won FREE CASH now!!!

    Click here:
    http://spam.com

    """

    cleaned = preprocess_text(
        sample_email
    )

    assert isinstance(
        cleaned,
        str
    )

    assert len(cleaned) > 0