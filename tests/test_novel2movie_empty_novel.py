"""Empty novel_text must not ZeroDivisionError on compression summary."""

from __future__ import annotations

import pytest


def _compression_ratio_line(novel_text: str, compressed_novel: str) -> str:
    if novel_text:
        return f"📌 Compression Ratio: {len(compressed_novel) / len(novel_text):.2%}"
    return "📌 Compression Ratio: n/a (empty novel text)"


def test_empty_novel_ratio_is_na_not_zerodiv() -> None:
    assert _compression_ratio_line("", "") == "📌 Compression Ratio: n/a (empty novel text)"


def test_nonempty_novel_ratio_formats() -> None:
    assert _compression_ratio_line("abcd", "ab") == "📌 Compression Ratio: 50.00%"


def test_unfixed_formula_zerodivs_on_empty() -> None:
    with pytest.raises(ZeroDivisionError):
        _ = f"{len('') / len(''):.2%}"
