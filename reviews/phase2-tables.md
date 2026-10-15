# Independent review of all ten source tables

16 October 2026. Reviewer `/root/bijections_phase2`, requested by coordinator after the table implementation was supplied. Reviewed `experiments/table_audit.py`, `experiments/tests/test_tables.py`, `experiments/source_tables.json`, ignored original `ham-2019.pdf` and its `ham-bbox.html` extraction. Used the PDF skill for read-only source rendering. No other table review was read. This is internal AI review, not external peer review or human author approval.

**Verdict: pass the claim that all 697 printed numerical body entries in Tables 1–10 match independently recomputed counts after assigning horizontal coordinates by column position, with the two printed axis defects separately retained.** This does not validate a claimed OEIS identity, every blank cell as a printed zero, or every surrounding source conjecture.

## Source extraction completeness and source identity

I independently computed the PDF SHA-256 and verified it equals the `source_sha256` recorded in the JSON (`7cd60b318fdaed8fd9c5c3e76a56b626fa83c2dc6d94217bef0c437a6f17138a`). The source PDF remains in the ignored cache.

I independently remapped **every numerical table body token** from the PDF bounding-box extraction. For each table I located its x-axis marker, read the axis numerical labels in spatial order, identified the y-axis numeric row labels, and assigned body tokens to their nearest column right edge and row baseline. Column right edges are used because the source values are right aligned; numeric center coordinates shift with digit count. This calculation did not use the count engine. The resulting coordinate/value triples agreed exactly, as sets, with the JSON for all ten tables. Source body counts are:

| Table | PDF page | Printed numerical body entries |
|---|---:|---:|
| 1 | 8 | 64 |
| 2 | 8 | 51 |
| 3 | 9 | 45 |
| 4 | 9 | 82 |
| 5 | 9 | 78 |
| 6 | 10 | 106 |
| 7 | 10 | 105 |
| 8 | 10 | 66 |
| 9 | 11 | 49 |
| 10 | 11 | 51 |
| Total | | 697 |

Every table has distinct stored (x,y) coordinates; no duplicate entries inflate the total. The remapping also independently reproduced every `printed_x_labels` list. This is an exhaustive numeric-token extraction check against the PDF text layer, supplemented by the visual sample below; it is not a claim of manually reading all 697 values from raster images.

I rendered source PDF page 10 with Poppler and viewed the complete resulting PNG. It contains Tables 6, 7 and 8 with their captions. In both Tables 6 and 7 the horizontal positions read 0,...,12,12,14: the second printed 12 occupies coordinate position 13. The source's duplicate-label defect is visible, not inferred solely from DP disagreement. The JSON preserves it separately while assigning numeric coordinates by spatial order. Visible source examples, including the Table 6 axis tail 4213,11298,30537 and Table 8 axis tail 20793,103049,518859, agree with the extracted facts.

## Counting audit

- **Tables 1–3,5,8–10:** Each upstep is (1,1); every other step is a strictly negative vertical jump. Therefore every visited height lies in 0<=y<=x. Ordering states by increasing x and, within a column, decreasing y is acyclic. The recurrence takes its upstep predecessor from (x-1,y-1) and its vertical predecessors from (x,z), z>y, exactly once per allowed distinct jump. The empty path appears once at (0,0). The allowed-drop predicates correctly match each table caption.
- I independently enumerated actual finite words for all seven vertical models through horizontal column 5, and compared every endpoint in the final column with the implementation: **42 model/column comparisons passed**. Unlike the committed test, this review experiment covered Tables 2,3 and9 as well. The recursive enumeration records a path whenever it reaches x=n and continues through possible vertical suffixes, so it correctly counts words ending at different heights and does not prematurely stop at the last upstep.
- **Tables 4 and6:** Upsteps have height +1 and all other increments are strictly negative; no reachable height exceeds x. The finite unit-horizontal domain is therefore exact.
- **Table 7:** Its +k jumps make a naive height<=x bound false. The implementation instead uses cap=Y+n when checking endpoints <=Y through column n. If a path ending at height y<=Y reaches intermediate height h after k steps, its remaining n-k steps can lower height by at most n-k, because its only negative increment is -1. Thus h<=y+n-k<=Y+n. Every path contributing to the requested endpoints lies inside the cap; paths rising above it cannot return in time. This proves the truncation exact, without assuming a finite positive jump set.
- For Table 7 I independently generated actual height-increment words through length 5, with requested endpoints 0,...,4 and the proved finite bound. All **30 endpoint comparisons passed**, including the empty path and zero inaccessible endpoints.

The existing two table unittest methods pass when invoked from the repository root as `python3 -m unittest experiments.tests.test_tables`. The direct `check_tables()` result is exactly `(697, [], [(6,13,12),(7,13,12)])`.

## Limitations

The numerical facts are transcribed from the original PDF's text layer, whose table geometry was checked independently, with a visual sample of one full page. No automated OCR or full manual raster transcription was performed. No downloaded source PDF was added to tracked files. The table check establishes the finite source arrays on the precise stated coordinate convention; matching a sequence name or proving a formula requires the separate mathematical arguments and literature audit.
