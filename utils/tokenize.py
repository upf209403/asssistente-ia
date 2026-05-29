import re
from normalize_text import normalize_text

def tokenize(text: str):
    normalized = normalize_text(text)

    return re.findall(
        r"\b\w+\b",
        normalized
    )