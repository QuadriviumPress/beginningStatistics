# Sources and Attribution

## Primary text

This edition adapts [Beginning Statistics, version 1.0](https://2012books.lardbucket.org/books/beginning-statistics/), preserved by Andy Schmitz on December 29, 2012. The [offline archive](https://2012books.lardbucket.org/zips/beginning-statistics.zip) was retrieved November 3, 2026; SHA-256: `85db542c75ca7543532329829571d59a332068fd6922751c6cde51630431f7eb`.

The content retains [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/). The source requests omission of customary attribution to the original authors and publisher. That notice is reproduced in [the license page](front/license.md); source biographical material is preserved as supplied. QuadriviumPress is credited for this MyST adaptation, not as the author of the original textbook.

All eleven chapters, About the Authors, Acknowledgements, Dedication, Preface, and the Appendix are imported. The table of contents and all 16 combined source pages are archived in `source/`. `source/manifest.json` records source and output checksums and the per-page counts of images, MathML expressions, HTML tables, questions, and answer slots. Both section-page and combined-chapter links are rewritten to local chapter targets, with source identifiers retained as labels.

## Figures and reference tables

All 145 image slots were reviewed in contact sheets. The 143 instructional diagrams and statistical table scans have no separate third-party rights notice and retain the textbook license. All 128 diagrams are redrawn as accessible SVG by `scripts/render_figures.py` (see below). The 13 appendix table scans and two images of single equations are copied byte-for-byte at their original resolution. The two author photographs lack separate rights documentation; original typographic name cards replace them. These cards are created by QuadriviumPress under CC BY-NC-SA 3.0 and do not depict the authors. Restricted original portrait bytes are excluded from this edition.

[Image credits](image-credits.md) lists every slot; the [figure audit](FIGURE-AUDIT.md) documents the review and limitations. `figure-replacements.json` records portrait replacement paths, source and output hashes, alternative text, credit, and license. `source/manifest.json` records provenance for every delivered asset. Appendix probability and critical-value tables retain their original raster scans; the numeric cells are not accessible as semantic tables.

## Conversion and editorial policy

Seeded from [opiniatedMystmdBookTemplate](https://github.com/QuadriviumPress/opiniatedMystmdBookTemplate). The importer and rendered-content audit are adapted from QuadriviumPress’s chemistry editions. Publisher layout is replaced by MyST headings, callouts, figures, list tables, footnotes, and local links. MathML becomes TeX, including expressions embedded in callout titles. Unsupported Pandoc division and spacing commands are normalized to equivalent KaTeX-compatible notation; typographic thin spaces become ordinary spaces. Heading and figure numbering remains literal to preserve source references. One malformed source equation in Section 10.3 (`fwk-shafer-ch10-m0105`) used rowless MathML tables to draw boxes around the deterministic term and noise term. The importer changes these into valid boxed enclosures, retaining the equation and both boxes. Glossary definitions become footnotes. Answers become expandable groups, preserving original numbering and empty answer slots.

The textbook is a source adaptation, not a new statistical content revision. Source-era examples, numerical answers, terminology, and teaching conventions are retained. No full mathematical or statistical audit is claimed. Any later corrections must be documented here and applied reproducibly by `scripts/import_source.py`, with source-drift checks.

### SVG redraws (2026-11-04)

`scripts/render_figures.py` redraws source diagrams as SVG using only the Python standard library; the importer installs each redraw in place of its source raster and records both checksums in `figure-replacements.json`. The redraws cover every diagram in Chapters 1–11: 128 figures. Curves are computed from the densities they show (normal, Student *t*, chi-square, *F*, uniform, and, for the schematic skewed curve of Figure 5.19, a gamma density), and z values sit at their true positions. The source draws every chi-square and *F* test with the same generic curve; the redraws use the true density for each example’s degrees of freedom, with critical values at their true positions (each checked against its stated α), so curves with 1 or 2 degrees of freedom are highest at 0 and tails of area 0.01 are thin. The generic illustrations (Figures 11.2, 11.8, and 11.9) use a chi-square density with 5 degrees of freedom and *F* densities with (10, 15) and (15, 20) degrees of freedom. The 40 intervals of Figure 7.2 are measured from the source image, so the redraw shows the same simulated sample, including the two intervals that miss μ. Data plots are computed from the data printed in the text: the stem and leaf diagrams and histograms of the 30 test scores (Figures 2.1–2.4), the 100 heights of Table 2.2 in half-inch classes from 65.5 inches (Figure 2.15), the dot plots of Table 2.1, the box plot of Example 14, the probability distributions of Chapter 4 (Figure 4.5 is binomial with n = 5 and p = 0.17), the sampling distributions of Chapter 6 (computed exactly by convolution in Figure 6.3), and the scatter plots of Tables 10.3, 10.4, and the height–weight data, with the least squares lines computed from the data. Scatter plots and histograms that illustrate a shape rather than a data set (Figures 2.5, 4.6, 10.3, 10.4, and 10.11) are measured from the source images; the printed correlation coefficients in Figure 10.4 agree with the measured points to within 0.01. Concept sketches (Figures 2.6–2.9, 2.11, 2.12, 2.19, and similar) use normal or gamma densities or mixtures of normals; medians, modes, means, and standard deviations marked on them are computed from the curve drawn. Test statistics beyond the drawn range (Z = 5.684 in Figures 9.2 and 9.3; χ² = 31.75 and 651.881 in Figures 11.4 and 11.6) are marked near the right end, as in the source. Student *t* figures are schematic, as in the source: each *t* value is placed where the drawn curve encloses the tail area of the *t* distribution with the stated degrees of freedom. Every label was checked against the source figure and its worked example. Each redraw replaces the generic “Statistical diagram” alternative text with a full description.

Three other source errors are corrected: the box plot for Example 14 marked the median as 2.63, but the text computes Q₂ = 2.62; Figure 2.18(b) labeled the area above 130 as ≈ 0.015%, but the text gives 15/100 of 1%, that is, 0.15%; and the Example 21 illustration captioned its second panel “Outside x̄ ± 2”, now “Outside x̄ ± 2s”. Stray spaces inside two printed numbers (“0 .9452” in Figure 5.11 and “0 .75” in Figure 5.27) are removed. One source error is corrected. Figure 8.16 (Example 13, a test at α = 0.10) labeled each tail “α/2 = 0.005” beside critical values ±1.645. The redraw labels each tail α/2 = 0.05, matching the example’s α and its critical values.

The inline equation image after Section 8.5's conditions (`712af0ac`) is a formula, not a diagram, and remains a source raster.

### Editorial corrections (2026-11-03)

`scripts/content_corrections.py` runs at the end of every import. It applies high-confidence proofreading fixes found in a fleet grammar pass and normalizes British spellings to American English (fleet convention). Summary:

- **Typos:** `Probablity` → Probability; `Univeristy` → University; `exercsises`, `deciaml`, `buyers's`, `predominately`; doubled words (`to to`, `all all`, `the their`); `{0.1.2}` → `{0,1,2}`.
- **Grammar and wording:** subject–verb agreement (`A list … is`, `The set of assumptions … is`, `numbers forms`); missing words (`confidence interval for`, `Find the percentage`, articles); wrong forms (`must first compute`, `selected at random`, `*X* lies`, `hypothesis testing`, `freshmen`, `An investigator` / `An automotive`); `neither … nor`; `every day`; `test booklet`; `paired sampling`; `ensure` where “make certain” is meant.
- **Content:** *t<sub>c</sub>* defined on Student’s *t*-distribution (not the standard normal); event label `P(MF)` for the MF event; agency name National Institutes of Health with definite articles.
- **American spelling:** Modelling/modelling → Modeling/modeling; travellers/travelling; judgement; Acknowledgements → Acknowledgments (filename `front/acknowledgements.md` kept as the source slug); cancelling → canceling.
- **Truncated xref titles** already broken in the 2012 HTML restored for Figures 7.5, 10.6, 11.1, 11.7 and the Chapter 11 self-reference. Other titles that drop inline math (`Critical Values of `, and similar) remain as in the source archive.

No third-party simulations or interactive activities are embedded. The template provides navigation, search, and offline access to previously visited pages.

## Missing companion data

The preserved archive contains no companion spreadsheets for the exercises labeled “Large Data Set Exercises.” Those prompts are preserved, but cannot be completed from this edition alone without separately supplied data. This limitation is disclosed on the landing page. No synthetic data have been substituted for the original observations.

## Template code

The build configuration, PWA shell, and tooling originate in the QuadriviumPress MyST template. The MIT notice is retained in [LICENSE-CODE](LICENSE-CODE). The book-specific histogram-and-curve SVG branding is original QuadriviumPress artwork under CC BY-NC-SA 3.0.
