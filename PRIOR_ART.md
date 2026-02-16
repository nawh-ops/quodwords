
Prior Art Disclosure: Alternative Encoding Forms

This document records alternative encoding forms explored during the early design of QuodWords, disclosed here as prior art.

These forms are not required for the reference implementation and are not currently part of the default public API, but they represent equivalent coordinate encodings over the same underlying spatial grid.

This disclosure is intended to establish public prior art and clarify design scope.

1. Phonetic Alphabet Encoding

In addition to word-list encodings, QuodWords has explored the use of phonetic alphabet tokens as spatial identifiers.

Characteristics

Uses internationally recognised phonetic words (e.g. NATO phonetic alphabet)

Optimised for:

spoken communication

radio / voice transmission

noisy or low-bandwidth environments

Reduces ambiguity compared to spelling individual letters

Conceptual Example

A spatial cell may be represented as:

Foxtrot.Alpha.Tango


Spoken as:

“Foxtrot Alpha Tango”

This form represents the same underlying spatial cell as a word-based encoding, differing only in token vocabulary.

2. Phonetic + Numeric Encoding (Mixed-Mode)

A further explored variant combines phonetic tokens with numeric components.

This form is designed to:

increase address space density

shorten total spoken length

maintain clarity in verbal transmission

Conceptual Structure
<Phonetic>.<Phonetic>.<Phonetic>.<Digit>.<Digit>


or spoken without separators as:

“Foxtrot Alpha Tango Three Two”

Worked Example
Foxtrot.Alpha.Tango.3.2


Spoken as:

“Foxtrot Alpha Tango Three Two”

This represents a finer-resolution spatial cell derived from the same hierarchical grid as word-only encodings.

3. Spoken-First Design Considerations

These alternative encodings were explored with the following constraints:

All tokens must be:

unambiguous when spoken

distinct under common accents

resistant to truncation or noise

Numeric components are always spoken digit-by-digit:

“Three Two” (not “Thirty-Two”)

Separators (e.g. dots) are conceptual and may be spoken as:

“dot”

“decimal”

or omitted entirely in controlled contexts

4. Relationship to Word-Based Encodings

All alternative forms described here:

map to the same spatial grid

preserve one-to-one reversibility

differ only in token vocabulary, not spatial logic

They should be understood as encoding modes, not separate systems.

5. Status

These encoding forms are:

disclosed as prior art

intentionally non-exclusive

not asserted as patented or proprietary

subject to future inclusion or exclusion at the discretion of the project

6. Disclosure Intent

This document exists to:

establish early public disclosure

prevent future novelty claims over equivalent phonetic or mixed-mode encodings

clarify the conceptual scope of QuodWords

No claim is made that these forms are superior to, or preferred over, word-only encodings.

These disclosures are made without restriction, licence requirement, or expectation of exclusivity.