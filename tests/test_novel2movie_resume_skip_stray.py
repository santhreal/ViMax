"""Resume cache listing must skip non chunk-*-score_*.txt files."""

from __future__ import annotations

from pathlib import Path


def test_pipeline_skips_non_score_filenames() -> None:
    src = Path("pipelines/novel2movie_pipeline.py").read_text(encoding="utf-8")
    assert src.count('if "-score_" not in chunk_fname or not chunk_fname.endswith(".txt")') == 2


def test_stray_name_indexerrors_without_guard() -> None:
    try:
        float("notes.txt".split("-score_")[1].split(".txt")[0])
        ok = False
    except IndexError:
        ok = True
    assert ok
