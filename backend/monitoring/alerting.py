# =========================================================
# ALERT SYSTEM
# =========================================================

def generate_alert(

    system_status
):

    if system_status == "CRITICAL":

        return "🚨 Critical drift detected!"

    elif system_status == "WARNING":

        return "⚠️ Moderate drift detected."

    return "✅ System stable."