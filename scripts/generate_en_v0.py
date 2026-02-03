#!/usr/bin/env python3
"""
Generate the canonical English v0 wordlist for QuodWords.

Design goals:
- Conservative, common English words only
- Deterministic output (same input -> same file forever)
- ASCII lowercase only
- One word per line
- Immutable once published
"""

from pathlib import Path
from wordfreq import zipf_frequency

# ===== CONFIG =====

LANG = "en"
TARGET_COUNT = 4096          # exactly 4096 words
MIN_ZIPF = 4.0               # conservative/common threshold
MAX_WORD_LEN = 12            # avoid long/awkward words

OUTPUT_PATH = Path("wordlists/en_v0.txt")

# ==================


def is_clean_word(word: str) -> bool:
    """Strict filter for safe, boring, common words."""
    if not word.isascii():
        return False
    if not word.islower():
        return False
    if not word.isalpha():
        return False
    if len(word) < 2 or len(word) > MAX_WORD_LEN:
        return False
    return True


def main():
    # wordfreq doesn't give a raw list, so we iterate over possible words
    # by scanning frequency space deterministically
    candidates = []

    # This is deterministic because zipf_frequency is stable
    # and we sort explicitly.
    for letter1 in "abcdefghijklmnopqrstuvwxyz":
        for letter2 in "abcdefghijklmnopqrstuvwxyz":
            prefix = letter1 + letter2
            freq = zipf_frequency(prefix, LANG)
            if freq >= MIN_ZIPF:
                candidates.append(prefix)

    # Expand by scanning wordfreq internally
    # We rely on wordfreq's internal lexicon determinism
    from wordfreq import top_n_list

    words = top_n_list(LANG, 50000)

    for word in words:
        if not is_clean_word(word):
            continue
        if zipf_frequency(word, LANG) < MIN_ZIPF:
            continue
        candidates.append(word)

    # Deduplicate, sort deterministically
    final = sorted(set(candidates))

    if len(final) < TARGET_COUNT:
        raise RuntimeError(
            f"Only {len(final)} words found — adjust MIN_ZIPF if needed"
        )

    final = final[:TARGET_COUNT]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(final) + "\n", encoding="utf-8")

    print(f"Wrote {len(final)} words to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
