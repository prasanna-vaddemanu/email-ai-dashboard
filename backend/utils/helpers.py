from datetime import datetime


# =========================================================
# TIMESTAMP
# =========================================================

def current_timestamp():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


# =========================================================
# FORMAT PERCENTAGE
# =========================================================

def format_probability(probability):

    return f"{probability:.2%}"


# =========================================================
# THREAT COLOR
# =========================================================

def threat_color(level):

    if level == "HIGH":

        return "red"

    elif level == "MEDIUM":

        return "orange"

    return "green"