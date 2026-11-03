# Validation report

Validated November 3, 2026, with Node 26.13.0 and MyST 1.12.0.

## Coverage

| Component | Source | Rendered |
| --- | ---: | ---: |
| Top-level imported source pages | 16 | 16 |
| Chapters | 11 | 11 |
| HTML tables | 133 | 133 |
| Image slots | 145 | 145 |
| Nonempty mathematical expressions | 4,615 | 4,617 |
| Numbered and bulleted list items | 4,896 | 4,896 |
| Question slots | 925 | Source numbering retained |
| Answer slots, including intentionally empty slots | 925 | Source numbering retained |

The site contains 21 pages in total, including the landing page, license, provenance, credits, and audit. All 262 explicitly referenced source targets resolve locally. The rendered audit rejects lost tables, images, mathematical expressions, list items, and prose parsed as code.

## Checks performed

- `npm ci --offline --no-audit --no-fund`: installed the committed lockfile successfully.
- `BASE_URL=/beginningStatistics npm run check`: strict HTML build, internal references, source checksums, content coverage, and PWA asset setup passed.
- Repeated import from the preserved archive: byte-for-byte comparison of all project files, excluding caches, dependencies, and build output, returned no differences.
- Deliberately altered source index: importer rejected source drift before writing output.
- Bindery catalog schema/invariants and repository compliance: passed, with zero compliance failures or warnings.
- Chromium desktop checks: landing page, chapters 2, 7, and 10, and the appendix loaded with no broken images or KaTeX errors.
- Desktop and 390-pixel mobile screenshots reviewed; navigation and content render correctly.
- PWA registration uses `/beginningStatistics/`. A previously visited regression chapter reloaded offline with all 16 displayed images intact.
- Source photographs are excluded by checksum; replacement name cards retain visible credits. Retained teaching artwork is copied byte-for-byte.

## Conversion repairs and limits

Callout-title math is retained. KaTeX-incompatible Pandoc spacing and division commands are normalized. The malformed boxed regression equation in Section 10.3 is repaired using valid MathML enclosures. Empty answer placeholders remain explicit, preserving nested list indentation without trailing whitespace. The source archive and importer document these changes reproducibly.

MyST prints image-size advisories for the 13 large appendix table scans; original resolution is intentionally preserved for legibility. The strict content build has no unresolved mathematical or internal-link errors.

The source archive lacks companion spreadsheets referenced by “Large Data Set Exercises”; their prompts are retained and the limitation is disclosed to readers. Table scans do not expose their numeric cells to screen readers. This validation checks import and rendering fidelity, not every statistical assertion or numerical answer in the 2012 source.

## Publication state

The book uses `QuadriviumPress/beginningStatistics` on branch `main`, with GitHub Actions publishing to [the online textbook](https://quadriviumpress.com/beginningStatistics/). The deployment runs the strict build and rendered-content checks. Bindery and the public book listings use this canonical URL.
