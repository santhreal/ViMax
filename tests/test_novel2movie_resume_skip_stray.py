"""Resume cache listing must skip non chunk-*-score_*.txt files."""

from __future__ import annotations

import tempfile
from pathlib import Path

from utils.text import _iter_score_chunk_files


def test_stray_notes_only_dir_yields_no_scores() -> None:
    with tempfile.TemporaryDirectory() as d:
        Path(d, "notes.txt").write_text("x", encoding="utf-8")
        assert list(_iter_score_chunk_files(d)) == []


def test_valid_chunk_file_is_yielded() -> None:
    with tempfile.TemporaryDirectory() as d:
        Path(d, "notes.txt").write_text("x", encoding="utf-8")
        Path(d, "chunk_0-score_0.85.txt").write_text("chunk body", encoding="utf-8")
        got = list(_iter_score_chunk_files(d))
        assert len(got) == 1
        path, score = got[0]
        assert score == 0.85
        assert Path(path).read_text(encoding="utf-8") == "chunk body"


def test_unfixed_split_indexerrors_on_stray() -> None:
    try:
        float("notes.txt".split("-score_")[1].split(".txt")[0])
        ok = False
    except IndexError:
        ok = True
    assert ok
