"""Regression: empty novel_text must not ZeroDivisionError in summary."""

from __future__ import annotations

from utils.text import format_compression_ratio


def test_empty_novel_ratio_is_na() -> None:
    assert format_compression_ratio("", "") == "n/a (empty novel text)"


def test_normal_novel_ratio() -> None:
    assert format_compression_ratio("abcd", "ab") == "50.00%"
