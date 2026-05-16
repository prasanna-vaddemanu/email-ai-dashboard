import os
import pandas as pd

from datetime import datetime


# =========================================================
# LOG FILE PATH
# =========================================================

LOG_PATH = "logs/predictions.csv"


# =========================================================
# CREATE CSV IF NOT EXISTS
# =========================================================

def initialize_metrics_file():

    os.makedirs(
        "logs",
        exist_ok=True
    )


    if not os.path.exists(LOG_PATH):

        df = pd.DataFrame(

            columns=[

                "timestamp",

                "prediction",

                "label",

                "spam_probability",

                "risk_score",

                "threat_level"
            ]
        )

        df.to_csv(

            LOG_PATH,

            index=False
        )


# =========================================================
# SAVE PREDICTION
# =========================================================

def log_prediction(

    prediction,

    label,

    spam_probability,

    risk_score,

    threat_level
):

    initialize_metrics_file()


    new_data = {

        "timestamp": datetime.now(),

        "prediction": prediction,

        "label": label,

        "spam_probability": spam_probability,

        "risk_score": risk_score,

        "threat_level": threat_level
    }


    df = pd.read_csv(
        LOG_PATH
    )


    df = pd.concat(

        [

            df,

            pd.DataFrame([new_data])
        ],

        ignore_index=True
    )


    df.to_csv(

        LOG_PATH,

        index=False
    )


# =========================================================
# LOAD METRICS
# =========================================================

def load_metrics():

    initialize_metrics_file()

    return pd.read_csv(
        LOG_PATH
    )