from backend.core.threat_scoring import (
    calculate_risk_score
)


# =========================================================
# TEST THREAT SCORING
# =========================================================

def test_risk_score():

    sample_email = """

    FREE CASH!!!

    Click now!!!

    http://spam.com

    """

    result = calculate_risk_score(
        sample_email
    )

    assert isinstance(
        result,
        dict
    )

    assert "risk_score" in result

    assert "threat_level" in result

    assert result["risk_score"] >= 0