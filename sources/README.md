# Source register and provenance

Recorded 16 October 2026 (Australia/Melbourne). The original documents and historical code are reference material, distinct from this project's independently written experiments and proofs.

The ignored directory `.local/references/` contains the two downloaded PDFs, layout-preserving `pdftotext` extractions, and an original-code clone. These reference caches are not redistributed by committing them. No licence for redistributing the PDFs has been established in this session. The bibliographic links below remain the reproducible public entry points; hashes identify the exact local bytes inspected, not an assurance that remote files will stay unchanged.

| Artifact | Public source | Local reference cache | SHA-256 |
|---|---|---|---|
| Ham, 2019, PDF | [Lattice path conjectures](https://n-ham.com/old-website/pdfs/Lattice%20Path%20Conjectures.pdf) | `.local/references/ham-2019.pdf` | `7cd60b318fdaed8fd9c5c3e76a56b626fa83c2dc6d94217bef0c437a6f17138a` |
| Ham, extracted text | Derived from preceding PDF using `pdftotext -layout` | `.local/references/ham-2019.txt` | `edc31ddefa4ba9c4df3416fcfc1d3c13cfd98c314c89dc6d9a8dd60318d1b281` |
| East–Ham, arXiv v3 PDF | [arXiv:1811.05735](https://arxiv.org/abs/1811.05735), [PDF](https://arxiv.org/pdf/1811.05735) | `.local/references/east-ham.pdf` | `328ccb8b369e6931091a7c99b60f6e615107c29a74c55af6bc0dafeba722879f` |
| East–Ham, extracted text | Derived from preceding PDF using `pdftotext -layout` | `.local/references/east-ham.txt` | `8063be090e7432153a589e8d0f241bd9895e4c992472108fcec72804d33c4173` |

Ham's PDF has 11 pages and the visible date 11 May 2019. All 626 extracted text lines were read, including every section 1–41, all ten arrays, their captions, and the references. The raw text extraction of PDF page 7 was additionally inspected to resolve the cubic in section 35: `(4/3)x^3 - 2x^2 + (11/3)x - 1`. This was text-level source inspection, not a visual-layout audit or independent recomputation of the arrays.

The East–Ham cached PDF identifies itself as `arXiv:1811.05735v3 [math.CO], 27 May 2021`. Cite that version when discussing its exact results. The 2019 conjecture document's reference calls East–Ham a 2015 preprint; this is not the arXiv deposit date or cached version date. The historical algorithms correspond to an earlier manuscript version; see the separate detailed audit before matching algorithm numbers to v3.

The public [original algorithm repository](https://gitlab.com/n-ham-paper-files/lattice-path-algorithms) was successfully cloned and inspected at commit `e470a327c0f9fa29f52cd9b287bfc132af7a6749`. Its declared licence is CC BY-SA 4.0, copyright 2018 Nicholas C. Ham. No original implementation was copied into the new project source. [algorithms-audit.md](algorithms-audit.md) records inspected files, build/smoke tests, explicit small checks, and observed or potential limitations.

The complete source-claim inventory lives in `research/conjecture-inventory.md` and the companion JSON. Its zero verified-term entries deliberately separate extraction from independent experimental evidence. New proof and numerical evidence belong in the conjecture audit and reproducible test suite. Source OEIS identifiers have all been preserved, but their current entries and definitions have not all been independently checked.
