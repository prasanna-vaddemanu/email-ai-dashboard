import re


# =========================================================
# URL DETECTION
# =========================================================

def extract_urls(text):

    urls = re.findall(

        r"http[s]?://\S+",

        str(text)
    )

    return urls


# =========================================================
# HTML DETECTION
# =========================================================

def html_tag_count(text):

    html_tags = re.findall(

        r"<[^>]+>",

        str(text)
    )

    return len(html_tags)


# =========================================================
# IFRAME DETECTION
# =========================================================

def iframe_count(text):

    text = str(text).lower()

    return text.count("<iframe")


# =========================================================
# UPPERCASE ANALYSIS
# =========================================================

def uppercase_ratio(text):

    text = str(text)

    if len(text) == 0:

        return 0

    upper_chars = sum(
        c.isupper() for c in text
    )

    return upper_chars / len(text)


# =========================================================
# EXCLAMATION ANALYSIS
# =========================================================

def exclamation_count(text):

    return str(text).count("!")


# =========================================================
# AUTHENTICATION ANALYSIS
# =========================================================

def authentication_check(text):

    text_lower = str(text).lower()

    auth = {

        "spf_fail": False,

        "dkim_fail": False,

        "dmarc_fail": False
    }


    if "spf=fail" in text_lower:

        auth["spf_fail"] = True


    if "dkim=fail" in text_lower:

        auth["dkim_fail"] = True


    if "dmarc=fail" in text_lower:

        auth["dmarc_fail"] = True


    return auth


# =========================================================
# THREAT PATTERN DATABASE
# =========================================================

SUSPICIOUS_PATTERNS = {

    "phishing": [

        "verify",
        "confirm",
        "validate",
        "authenticate",
        "login",
        "password",
        "credential",
        "account suspended",
        "unusual activity",
        "service interruption"
    ],

    "urgency": [

        "urgent",
        "immediately",
        "asap",
        "now",
        "quickly",
        "final warning",
        "limited time"
    ],

    "financial": [

        "bank",
        "payment",
        "invoice",
        "transfer",
        "cash",
        "credit",
        "debit",
        "reward"
    ],

    "marketing": [

        "discount",
        "offer",
        "winner",
        "free",
        "bonus",
        "income",
        "investment",
        "business opportunity",
        "work from home"
    ]
}


# =========================================================
# PATTERN DETECTION
# =========================================================

def detect_patterns(text):

    text_lower = str(text).lower()

    detected = {}


    for category, words in SUSPICIOUS_PATTERNS.items():

        found = []


        for word in words:

            if word in text_lower:

                found.append(word)


        if len(found) > 0:

            detected[category] = found


    return detected


# =========================================================
# MAIN THREAT ENGINE
# =========================================================

def calculate_risk_score(text):

    risk_score = 0

    reasons = []

    score_breakdown = {}


    # =====================================================
    # URL ANALYSIS
    # =====================================================

    urls = extract_urls(text)

    url_count = len(urls)


    if url_count >= 5:

        risk_score += 30

        score_breakdown[
            "Multiple Suspicious Links"
        ] = 30

        reasons.append(
            "+ Multiple suspicious links"
        )

    elif url_count >= 2:

        risk_score += 20

        score_breakdown[
            "Multiple External Links"
        ] = 20

        reasons.append(
            "+ Multiple external links"
        )

    elif url_count >= 1:

        risk_score += 10

        score_breakdown[
            "External Link"
        ] = 10

        reasons.append(
            "+ External link detected"
        )


    # =====================================================
    # HTML ANALYSIS
    # =====================================================

    html_count = html_tag_count(text)


    if html_count >= 20:

        risk_score += 20

        score_breakdown[
            "Heavy HTML Content"
        ] = 20

        reasons.append(
            "+ Heavy HTML content"
        )


    # =====================================================
    # IFRAME ANALYSIS
    # =====================================================

    iframe_score = iframe_count(text)


    if iframe_score > 0:

        risk_score += 30

        score_breakdown[
            "Iframe Injection"
        ] = 30

        reasons.append(
            "+ Suspicious iframe detected"
        )


    # =====================================================
    # UPPERCASE ANALYSIS
    # =====================================================

    caps_ratio = uppercase_ratio(text)


    if caps_ratio >= 0.30:

        risk_score += 15

        score_breakdown[
            "Uppercase Abuse"
        ] = 15

        reasons.append(
            "+ Excessive uppercase usage"
        )


    # =====================================================
    # EXCLAMATION ANALYSIS
    # =====================================================

    exclamations = exclamation_count(text)


    if exclamations >= 5:

        risk_score += 15

        score_breakdown[
            "Excessive Exclamations"
        ] = 15

        reasons.append(
            "+ Excessive exclamation usage"
        )


    # =====================================================
    # AUTHENTICATION ANALYSIS
    # =====================================================

    auth = authentication_check(text)


    if auth["spf_fail"]:

        risk_score += 15

        score_breakdown[
            "SPF Failure"
        ] = 15

        reasons.append(
            "+ SPF authentication failed"
        )


    if auth["dkim_fail"]:

        risk_score += 10

        score_breakdown[
            "DKIM Failure"
        ] = 10

        reasons.append(
            "+ DKIM authentication failed"
        )


    if auth["dmarc_fail"]:

        risk_score += 10

        score_breakdown[
            "DMARC Failure"
        ] = 10

        reasons.append(
            "+ DMARC authentication failed"
        )


    # =====================================================
    # PATTERN ANALYSIS
    # =====================================================

    patterns = detect_patterns(text)


    if "phishing" in patterns:

        risk_score += 25

        score_breakdown[
            "Phishing Indicators"
        ] = 25

        reasons.append(
            "+ Phishing indicators detected"
        )


    if "urgency" in patterns:

        risk_score += 15

        score_breakdown[
            "Urgency Tactics"
        ] = 15

        reasons.append(
            "+ Urgency tactics detected"
        )


    if "financial" in patterns:

        risk_score += 15

        score_breakdown[
            "Financial Keywords"
        ] = 15

        reasons.append(
            "+ Financial keywords detected"
        )


    if "marketing" in patterns:

        risk_score += 10

        score_breakdown[
            "Marketing Spam"
        ] = 10

        reasons.append(
            "+ Marketing spam indicators"
        )


    # =====================================================
    # MAX SCORE LIMIT
    # =====================================================

    risk_score = min(
        risk_score,
        100
    )


    # =====================================================
    # THREAT LEVEL
    # =====================================================

    if risk_score >= 70:

        threat_level = "CRITICAL"

    elif risk_score >= 45:

        threat_level = "HIGH"

    elif risk_score >= 20:

        threat_level = "MEDIUM"

    else:

        threat_level = "LOW"


    # =====================================================
    # EMPTY REASONS
    # =====================================================

    if len(reasons) == 0:

        reasons.append(
            "No major suspicious indicators found."
        )


    # =====================================================
    # FINAL RESPONSE
    # =====================================================

    return {

        "risk_score": risk_score,

        "threat_level": threat_level,

        "reasons": reasons,

        "score_breakdown": score_breakdown,

        "detected_patterns": patterns,

        "url_count": url_count,

        "html_tag_count": html_count,

        "uppercase_ratio": round(
            caps_ratio,
            4
        ),

        "exclamation_count": exclamations
    }