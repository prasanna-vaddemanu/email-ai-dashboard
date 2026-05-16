import os
import joblib

from backend.utils.config import MODELS_DIR


# =========================================================
# LOAD VECTORIZER
# =========================================================

vectorizer = joblib.load(

    os.path.join(
        MODELS_DIR,
        "tfidf_vectorizer.pkl"
    )
)


# =========================================================
# VECTORIZE
# =========================================================

def vectorize_text(clean_text):

    return vectorizer.transform(
        [clean_text]
    )