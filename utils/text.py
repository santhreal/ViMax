import re


def safe_path_component(name) -> str:
    """Sanitize an LLM-derived identifier for use as a filesystem path component.

    Identifiers come from model output over user-supplied story text, so they may
    contain separators or traversal sequences; keep word characters (including
    CJK), dashes, dots and spaces, replace everything else, and strip leading
    dots so the result can never escape or hide within the working directory.
    """
    cleaned = re.sub(r"[^\w\-. ]", "_", str(name))
    cleaned = cleaned.strip().lstrip(".")
    return cleaned or "unnamed"


def format_compression_ratio(novel_text: str, compressed_novel: str) -> str:
    """Human-readable compression ratio; empty novel has no ratio."""
    if not novel_text:
        return "n/a (empty novel text)"
    return f"{len(compressed_novel) / len(novel_text):.2%}"
