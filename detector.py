"""Transparent baseline prompt-injection screening detector."""

import re

# Intentionally inspectable starter patterns, not a complete security solution.
INJECTION_PATTERNS = [
    re.compile(r"\bignore\s+(all\s+)?(previous|prior|above)\s+instructions?\b", re.I),
    re.compile(r"\b(reveal|show|print|share)\s+(the\s+)?(system prompt|hidden instructions|secret instructions)\b", re.I),
    re.compile(r"\bdeveloper message\b", re.I),
    re.compile(r"\b(jailbreak|DAN mode)\b", re.I),
    re.compile(r"\bdisregard\s+(all\s+)?(rules|instructions)\b", re.I),
]


def predict(text: str) -> int:
    """Return 1 when a prompt matches a starter injection pattern, else 0."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return int(any(pattern.search(text) for pattern in INJECTION_PATTERNS))
