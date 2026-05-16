from backend.core.prediction import (
    predict_email
)


# =========================================================
# TEST PREDICTION
# =========================================================

def test_predict_email():

    sample_email = """

    Congratulations!!!

    You won FREE CASH now!!!

    Click here immediately!!!

    """

    result = predict_email(
        sample_email
    )

    assert isinstance(
        result,
        dict
    )

    assert "prediction" in result

    assert "spam_probability" in result

    assert result["prediction"] in [0, 1]