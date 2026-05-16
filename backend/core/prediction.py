import os
import joblib

from backend.core.preprocessing import (
    preprocess_text
)

from backend.utils.config import (
    MODELS_DIR
)

from backend.utils.logger import (
    logger
)


# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load(

    os.path.join(
        MODELS_DIR,
        "spam_classifier_model.pkl"
    )
)

vectorizer = joblib.load(

    os.path.join(
        MODELS_DIR,
        "tfidf_vectorizer.pkl"
    )
)


# =========================================================
# SPAM THRESHOLD
# =========================================================

SPAM_THRESHOLD = 0.85


# =========================================================
# EMAIL PREDICTION
# =========================================================

def predict_email(text):

    try:

        # ======================================
        # PREPROCESS TEXT
        # ======================================

        clean_text = preprocess_text(
            text
        )


        # ======================================
        # VECTORIZATION
        # ======================================

        vectorized_text = vectorizer.transform(
            [clean_text]
        )


        # ======================================
        # SPAM PROBABILITY
        # ======================================

        probability = model.predict_proba(
            vectorized_text
        )[0][1]


        # ======================================
        # CUSTOM THRESHOLD PREDICTION
        # ======================================

        prediction = int(

            probability >= SPAM_THRESHOLD
        )


        # ======================================
        # LOG PREDICTION
        # ======================================

        logger.info(

            f"Prediction={prediction} | "

            f"SpamProbability={probability:.4f}"
        )


        # ======================================
        # RETURN RESULT
        # ======================================

        return {

            "clean_text": clean_text,

            "prediction": prediction,

            "spam_probability": round(
                float(probability),
                4
            ),

            "spam_threshold": SPAM_THRESHOLD
        }


    except Exception as e:

        logger.error(

            f"Prediction Error: {str(e)}"
        )

        raise