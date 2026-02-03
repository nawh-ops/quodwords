#!/usr/bin/env python3
"""
verify_wordlist.py

Verifies that a wordlist matches its recorded SHA256 checksum.
Intended for long-term reproducibility checks.

Usage:
  python scripts/verify_wordlist.py wordlists/en_v0.txt wordlists/en_v0.sha256
"""

import hashlib
import pathlib
import sys


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python verify_wordlist.py <wordlist> <sha256_file>")
        sys.exit(2)

    wordlist = pathlib.Path(sys.argv[1])
    checksum_file = pathlib.Path(sys.argv[2])

    if not wordlist.exists():
        raise FileNotFoundError(wordlist)

    if not checksum_file.exists():
        raise FileNotFoundError(checksum_file)

    expected = checksum_file.read_text().strip().split()[0]
    actual = sha256(wordlist)

    if actual != expected:
        print("❌ CHECK FAILED")
        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
        sys.exit(1)

    print("✅ CHECK PASSED")
    print(f"{wordlist.name} matches recorded SHA256")


if __name__ == "__main__":
    main()
