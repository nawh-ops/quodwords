# QuodWords Specification (v0)

This document defines the normative specification for QuodWords version 0.
It is intended for implementers who require deterministic, reproducible,
offline-compatible encoding and decoding behaviour.

The accompanying README.md provides conceptual and human-facing documentation.
Where conflicts arise, this SPEC.md takes precedence.

---

## 0. © 2026 RouteBuddy GIS Ltd.

The QUODWORDS name is a registered trademark of RouteBuddy GIS Ltd.

---

## 1. Scope and goals

QuodWords is a deterministic location encoding system that maps geographic
coordinates to short sequences of real words.

Design goals:

- Deterministic and reproducible across platforms
- Fully offline (no network access required)
- Human-readable and human-transmissible
- Stable under versioning (no silent changes)
- Simple to implement correctly

Non-goals:

- Compression efficiency
- Natural-language semantics
- Backward compatibility across major versions prior to v1.0

---

## 2. Coordinate domain

- Input coordinates are latitude and longitude in decimal degrees.
- Latitude range: −90.0 ≤ lat ≤ +90.0
- Longitude range: −180.0 ≤ lon ≤ +180.0

Inputs outside these ranges MUST be rejected.

---

## 3. Grid model

- The Earth is divided into a fixed, global grid.
- Each grid cell corresponds to exactly one QuodWord.
- The grid resolution is fixed per specification version.
- The mapping from coordinates → grid cell is deterministic and purely
  algorithmic.

Given the same coordinates and specification version, the same QuodWord
MUST always be produced.

---

## 4. Wordlist

### 4.1 Wordlist versioning

- Wordlists are versioned and immutable.
- Once published, a wordlist file MUST NOT be edited.
- Changes require a new file with a new version identifier
  (e.g. `en_v1.txt`).

### 4.2 v0 English wordlist

- File: `wordlists/en_v0.txt`
- Size: exactly 4096 words
- Encoding: UTF-8, lowercase ASCII
- Order: lexicographically sorted
- Integrity: verified by SHA256 checksum (`en_v0.sha256`)

Implementations MUST use the exact wordlist file for v0 compatibility.

---

## 5. Encoding process (normative)

Given latitude and longitude:

1. Validate coordinate ranges.
2. Map coordinates to a grid cell index.
3. Map the grid cell index deterministically to one or more word indices.
4. Resolve word indices against the selected wordlist.
5. Output the QuodWord as a dot-separated sequence of words.

No randomness, external state, or lookup services may be used.

---

## 6. Decoding process (normative)

Given a QuodWord:

1. Validate token count and word validity.
2. Resolve each word against the selected wordlist.
3. Reconstruct the grid cell index deterministically.
4. Return the representative coordinates for that grid cell.

Decoding MUST be the inverse of encoding for the same specification version
and wordlist.

---

## 7. Determinism guarantees

QuodWords v0 is fully deterministic:

- Same inputs → same outputs
- Same wordlist + version → same behaviour
- No dependence on time, locale, platform, or network access

Any change that affects output MUST require an explicit version increment.

---

## 8. Error handling

Implementations MUST:

- Reject invalid coordinates
- Reject unknown or misspelled words
- Reject incorrect token counts
- Prefer clear failure over ambiguous or “nearby” results

Small transcription errors SHOULD result in clearly invalid or distant
locations, not subtly incorrect nearby ones.

---

## 9. Spoken use (phonetic rendering)

Spoken rendering is a presentation layer and does not affect encoding.

When QuodWords are communicated verbally (e.g. radio, phone, in-field use),
the following rules apply:

- Tokens of length ≤ 3 characters MUST be spelled letter-by-letter using
  the NATO phonetic alphabet  
  (e.g. `aa` → “Alfa Alfa”, `abc` → “Alfa Bravo Charlie”).

- Tokens of length ≥ 4 characters SHOULD be spoken as normal English words  
  (e.g. `abandon`, `muscle`).

This rule ensures unambiguous verbal transmission regardless of accent,
language background, or abbreviation ambiguity.

---

## 10. Versioning policy

- This specification defines QuodWords version 0.
- Breaking changes require a new major version.
- No backward compatibility guarantees are implied prior to v1.0.
- Earlier versions SHOULD remain reproducible indefinitely.

---

## 11. Reference implementation

This repository contains a reference implementation intended to demonstrate
correct behaviour. Other implementations may vary internally but MUST produce
identical results when conforming to this specification.

---

End of specification.
