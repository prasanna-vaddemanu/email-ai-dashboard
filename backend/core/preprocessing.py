import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


# =========================================================
# DOWNLOAD NLTK RESOURCES
# =========================================================

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

# =========================================================
# NLP TOOLS
# =========================================================

stop_words = set(
    stopwords.words("english")
)

stemmer = PorterStemmer()


# =========================================================
# LOWERCASE
# =========================================================

def lowercase_text(text):

    return str(text).lower()


# =========================================================
# REMOVE URLS
# =========================================================

def remove_urls(text):

    return re.sub(
        r"http[s]?://\S+",
        "",
        str(text)
    )


# =========================================================
# REMOVE HTML
# =========================================================

def remove_html(text):

    return re.sub(
        r"<[^>]+>",
        " ",
        str(text)
    )


# =========================================================
# REMOVE PUNCTUATION
# =========================================================

def remove_punctuation(text):

    return text.translate(

        str.maketrans(
            "",
            "",
            string.punctuation
        )
    )


# =========================================================
# REMOVE DIGITS
# =========================================================

def remove_digits(text):

    return re.sub(
        r"\d+",
        "",
        str(text)
    )


# =========================================================
# TOKENIZATION
# =========================================================

def tokenize_text(text):

    return word_tokenize(text)


# =========================================================
# STOPWORD REMOVAL
# =========================================================

def remove_stopwords(tokens):

    return [

        word
        for word in tokens

        if word not in stop_words
    ]


# =========================================================
# STEMMING
# =========================================================

def stem_tokens(tokens):

    return [

        stemmer.stem(word)

        for word in tokens
    ]


# =========================================================
# FULL PIPELINE
# =========================================================

def preprocess_text(text):

    text = lowercase_text(text)

    text = remove_urls(text)

    text = remove_html(text)

    text = remove_punctuation(text)

    text = remove_digits(text)

    tokens = tokenize_text(text)

    tokens = remove_stopwords(tokens)

    tokens = stem_tokens(tokens)

    clean_text = " ".join(tokens)

    return clean_text