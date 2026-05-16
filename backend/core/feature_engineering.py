import re
import pandas as pd


# =========================================================
# FEATURE EXTRACTION
# =========================================================

def extract_email_features(text):

    text = str(text)

    features = {

        "link_count": len(
            re.findall(
                r"http[s]?://\S+",
                text
            )
        ),

        "body_length": len(text),

        "word_count": len(
            text.split()
        ),

        "uppercase_ratio": (

            sum(c.isupper() for c in text)

            / len(text)

            if len(text) > 0 else 0
        ),

        "exclamation_count": text.count("!"),

        "digit_count": sum(
            c.isdigit()
            for c in text
        )
    }

    return pd.DataFrame(
        [features]
    )