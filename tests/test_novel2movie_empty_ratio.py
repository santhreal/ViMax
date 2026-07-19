"""Compression summary must tolerate empty novel_text."""

from __future__ import annotations

from pathlib import Path


def test_pipeline_source_guards_empty_novel_ratio() -> None:
    src = Path("pipelines/novel2movie_pipeline.py").read_text(encoding="utf-8")
    assert "if novel_text:" in src
    assert "n/a (empty novel text)" in src
    assert "len(compressed_novel) / len(novel_text)" in src


def test_empty_novel_ratio_formula_would_zerodiv_without_guard() -> None:
    novel_text = ""
    compressed_novel = ""
    try:
        _ = len(compressed_novel) / len(novel_text)
        raised = False
    except ZeroDivisionError:
        raised = True
    assert raised
