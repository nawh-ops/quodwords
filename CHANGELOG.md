# Changelog

All notable changes to the QuodWords reference implementation will be documented
in this file.

This project follows a deliberately conservative versioning approach. Changes
that affect determinism, encoding rules, wordlists, or decoding behaviour are
always explicit and versioned.

---

## [v0.0.0] – Initial reference implementation

### Added
- Initial QuodWords reference specification (`SPEC.md`).
- Top-level project overview and rationale (`README.md`).
- Deterministic English wordlist `en_v0.txt` (4096 words).
- SHA256 checksum for `en_v0.txt` to guarantee immutability.
- Wordlist verification script to validate frozen lists.
- Reference tooling for generating and validating wordlists.
- Clear spoken-use (phonetic rendering) rules for verbal transmission.

### Guarantees
- Deterministic encoding and decoding with no network access.
- Reproducible results when using the same specification version and wordlist.
- Explicit versioning for all future breaking changes.

### Notes
- Version `v0.0.0` represents a foundational, pre-1.0 reference release.
- No backward-compatibility guarantees are implied prior to `v1.0.0`.
- Earlier versions, once published, are intended to remain reproducible indefinitely.
