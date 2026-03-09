
## What is QuodWords?


QuodWords is an open, deterministic, human-readable location encoding system that converts geographic coordinates into short sequences of real words. Each QuodWord uniquely represents a fixed location on Earth and can be encoded and decoded without network access. The system is designed to be simple to implement, predictable in behaviour, and stable over time, making it suitable for mapping, navigation, outdoor activities, and location sharing where traditional latitude/longitude, plus-code style references, or proprietary location codes are inconvenient or error-prone.



## Project status (v0 series)

This repository is the **reference implementation** of QuodWords and its supporting artifacts.

- The normative rules live in **SPEC.md**.
- This code is intended to be **deterministic and reproducible** across implementations.
- The v0 series is **pre-1.0**: breaking changes may occur and will be explicitly versioned.

If you are looking for a production SDK, this repo is not that (yet).



## Why QuodWords exists

Sharing precise locations is still harder than it should be. Latitude and longitude are accurate but awkward for humans, easy to mistype, and difficult to communicate verbally. Many existing alternatives rely on proprietary services, opaque encoding schemes, or online lookups, which limits their usefulness in offline, outdoor, or low-connectivity situations. QuodWords exists to provide a simple, transparent, and offline-friendly way to refer to locations using ordinary words, while remaining deterministic, predictable, and straightforward for developers to implement.



## How QuodWords works

QuodWords works by dividing the surface of the Earth into a fixed, global grid and assigning word sequences to each grid cell in a deterministic way. Given a latitude and longitude, the same QuodWord will always be produced, and the original coordinates can be recovered from the QuodWord without reference to any external service.

Each QuodWord is constructed from a predefined list of ordinary words. The mapping between grid cells and word sequences is algorithmic rather than look-up based, which ensures that encoding and decoding can be performed entirely offline and implemented consistently across platforms and programming languages.

The system is designed so that small transcription errors result in clearly invalid or distant locations rather than subtly incorrect nearby ones. This prioritises clarity and safety over accidental plausibility when QuodWords are shared verbally, written down, or transmitted in constrained environments.



## Examples

The following examples illustrate the basic use of QuodWords for encoding and decoding locations.

### Encoding coordinates to a QuodWord

```
Latitude: 51.5074  
Longitude: -0.1278

QuodWord:  
harbour.lantern.slate
```

```
Input QuodWord:
harbour.lantern.slate

Decoded coordinates:
Latitude:  51.5074
Longitude: -0.1278
```



## Determinism and offline guarantees

QuodWords is fully deterministic: the same input coordinates will always produce the same QuodWord when using the same wordlist and version of the specification. No randomness, external state, or network access is involved in the encoding or decoding process.

All operations can be performed entirely offline. Encoding and decoding require only the QuodWords algorithm and the relevant wordlist, making the system suitable for use in environments with limited or no connectivity.

Changes to wordlists or encoding rules, if any, will be explicitly versioned to preserve reproducibility and prevent silent changes in behaviour.



## Versioning and stability

This repository represents a reference implementation of QuodWords version 0. The current version is provided to demonstrate the core concepts and behaviour of the system and may evolve as the specification is refined.

Breaking changes, including modifications to the wordlist, encoding rules, or output format, will only occur with an explicit version increment. Where possible, earlier versions will remain reproducible to support long-term use and testing.

No backward-compatibility guarantees are implied across major versions prior to a 1.0 release.

---

## License and trademark

The QuodWords reference implementation is released under the terms of the accompanying open-source license. See the `LICENSE` file for full details.

The name “QuodWords” and associated branding may be protected as trademarks. Use of the name does not imply endorsement or affiliation unless explicitly stated.




## Prior art and alternative encodings

This repository also documents earlier and alternative QuodWords encoding concepts, including alphanumeric and phonetic-based forms, disclosed for completeness and prior-art purposes.

See [`PRIOR_ART.md`](PRIOR_ART.md) for details and worked examples.


## List changes

If you change the list, it must be a new file: `en_v1.txt` — never edit `en_v0.txt`.




## Spoken use (phonetic rendering)

When QuodWords codes are communicated verbally (e.g. radio, phone, or in-field coordination), a fixed pronunciation protocol MUST be used to avoid ambiguity.

- Tokens of **length ≤ 3 characters** MUST be spelled letter-by-letter using the **NATO phonetic alphabet**  
    (e.g. `aa` → “Alfa Alfa”, `abc` → “Alfa Bravo Charlie”).
    
- Tokens of **length ≥ 4 characters** SHOULD be spoken as normal English words  
    (e.g. `abandon`, `muscle`).
    

This rule ensures unambiguous verbal transmission regardless of accent, language background, or whether a token resembles an abbreviation. The underlying wordlist remains language-agnostic; spoken rendering is treated as a separate presentation layer.


## Specification

The normative technical specification for the QuodWords encoding system is defined in:

SPEC.md
