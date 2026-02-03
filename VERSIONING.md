# Versioning Policy

QuodWords follows a deliberately conservative and explicit versioning policy.

The primary goal is **determinism and reproducibility** across implementations.

---

## Version series

### v0.x — Pre-1.0 reference series

The v0 series represents a **pre-1.0 reference implementation**.

- No backward-compatibility guarantees are implied.
- Breaking changes may occur between v0 releases.
- All breaking changes MUST result in a new explicit version.
- Earlier versions, once published, are intended to remain reproducible indefinitely.

This series exists to stabilise:
- Encoding rules
- Grid behaviour
- Wordlist structure
- Spoken-use conventions

---

### v1.0 and later

Version 1.0 will indicate:
- A stable, published specification
- Backward-compatibility guarantees within the major version
- Clear deprecation policies for future changes

Details for v1.x and later will be documented at the time of release.

---

## Wordlists and determinism

Any change to:
- Wordlists
- Encoding or decoding rules
- Grid resolution or ordering

**MUST** result in a new version.

This ensures identical inputs always produce identical outputs for a given version.

---

## Relationship to implementations

This repository defines the **reference behaviour**.

Other implementations:
- MAY differ internally
- MUST produce identical results when conforming to the same version
