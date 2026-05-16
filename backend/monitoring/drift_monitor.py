import pandas as pd

from scipy.stats import ks_2samp


# =========================================================
# FEATURE DRIFT DETECTION
# =========================================================

def detect_drift(

    reference_df,

    current_df,

    threshold=0.10,

    p_value_threshold=0.05
):

    drift_results = []


    # ======================================
    # LOOP FEATURES
    # ======================================

    for column in reference_df.columns:


        # ==================================
        # KS TEST
        # ==================================

        ks_statistic, p_value = ks_2samp(

            reference_df[column],

            current_df[column]
        )


        # ==================================
        # DRIFT STATUS
        # ==================================

        drift_detected = (

            (ks_statistic > threshold)

            and

            (p_value < p_value_threshold)
        )


        drift_results.append({

            "feature": column,

            "ks_statistic": round(
                ks_statistic,
                4
            ),

            "p_value": round(
                p_value,
                4
            ),

            "drift_detected": drift_detected
        })


    # ======================================
    # FINAL DATAFRAME
    # ======================================

    drift_df = pd.DataFrame(
        drift_results
    )


    return drift_df