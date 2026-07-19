"""Resume cache dirs may contain non-chunk files; skip them."""

from __future__ import annotations


def _parse_score(chunk_fname: str) -> float | None:
    if "-score_" not in chunk_fname or not chunk_fname.endswith(".txt"):
        return None
    return float(chunk_fname.split("-score_")[1].split(".txt")[0])


def test_stray_notes_file_skipped() -> None:
    assert _parse_score("notes.txt") is None


def test_valid_chunk_score_parsed() -> None:
    assert _parse_score("chunk_0-score_0.85.txt") == 0.85


def test_unfixed_split_indexerrors_on_stray() -> None:
    try:
        float("notes.txt".split("-score_")[1].split(".txt")[0])
        assert False, "expected IndexError"
    except IndexError:
        pass
