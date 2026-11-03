# Sources and Attribution

## Primary text

This edition adapts [Beginning Statistics, version 1.0](https://2012books.lardbucket.org/books/beginning-statistics/), preserved by Andy Schmitz on December 29, 2012. The [offline archive](https://2012books.lardbucket.org/zips/beginning-statistics.zip) was retrieved November 3, 2026; SHA-256: `85db542c75ca7543532329829571d59a332068fd6922751c6cde51630431f7eb`.

The content retains [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/). The source requests omission of customary attribution to the original authors and publisher. That notice is reproduced in [the license page](front/license.md); source biographical material is preserved as supplied. QuadriviumPress is credited for this MyST adaptation, not as the author of the original textbook.

All eleven chapters, About the Authors, Acknowledgements, Dedication, Preface, and the Appendix are imported. The table of contents and all 16 combined source pages are archived in `source/`. `source/manifest.json` records source and output checksums and the per-page counts of images, MathML expressions, HTML tables, questions, and answer slots. Both section-page and combined-chapter links are rewritten to local chapter targets, with source identifiers retained as labels.

## Figures and reference tables

All 145 image slots were reviewed in contact sheets. The 143 instructional diagrams and statistical table scans have no separate third-party rights notice and retain the textbook license. They are copied byte-for-byte at their original resolution. The two author photographs lack separate rights documentation; original typographic name cards replace them. These cards are created by QuadriviumPress under CC BY-NC-SA 3.0 and do not depict the authors. Restricted original portrait bytes are excluded from this edition.

[Image credits](image-credits.md) lists every slot; the [figure audit](FIGURE-AUDIT.md) documents the review and limitations. `figure-replacements.json` records portrait replacement paths, source and output hashes, alternative text, credit, and license. `source/manifest.json` records provenance for every delivered asset. Appendix probability and critical-value tables retain their original raster scans; the numeric cells are not accessible as semantic tables.

## Conversion and editorial policy

Seeded from [opiniatedMystmdBookTemplate](https://github.com/QuadriviumPress/opiniatedMystmdBookTemplate). The importer and rendered-content audit are adapted from QuadriviumPress’s chemistry editions. Publisher layout is replaced by MyST headings, callouts, figures, list tables, footnotes, and local links. MathML becomes TeX, including expressions embedded in callout titles. Unsupported Pandoc division and spacing commands are normalized to equivalent KaTeX-compatible notation; typographic thin spaces become ordinary spaces. Heading and figure numbering remains literal to preserve source references. One malformed source equation in Section 10.3 (`fwk-shafer-ch10-m0105`) used rowless MathML tables to draw boxes around the deterministic term and noise term. The importer changes these into valid boxed enclosures, retaining the equation and both boxes. Glossary definitions become footnotes. Answers become expandable groups, preserving original numbering and empty answer slots.

The textbook is a source adaptation, not a new statistical content revision. Source-era examples, numerical answers, terminology, and teaching conventions are retained. No full mathematical or statistical audit is claimed. Any later corrections must be documented here and applied reproducibly by `scripts/import_source.py`, with source-drift checks.

No third-party simulations or interactive activities are embedded. The template provides navigation, search, and offline access to previously visited pages.

## Missing companion data

The preserved archive contains no companion spreadsheets for the exercises labelled “Large Data Set Exercises.” Those prompts are preserved, but cannot be completed from this edition alone without separately supplied data. This limitation is disclosed on the landing page. No synthetic data have been substituted for the original observations.

## Template code

The build configuration, PWA shell, and tooling originate in the QuadriviumPress MyST template. The MIT notice is retained in [LICENSE-CODE](LICENSE-CODE). The book-specific histogram-and-curve SVG branding is original QuadriviumPress artwork under CC BY-NC-SA 3.0.
