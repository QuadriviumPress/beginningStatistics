# Beginning Statistics

A complete MyST Markdown adaptation of the 2012 *Beginning Statistics*, version 1.0: **11 chapters, four front-matter pages, and an appendix of statistical reference tables**. Seeded from QuadriviumPress’s `opiniatedMystmdBookTemplate`, following the chemistry editions.

The book covers descriptive statistics, probability, discrete and continuous random variables, sampling distributions, estimation, hypothesis tests, two-sample comparisons, regression, chi-square tests, and ANOVA. It retains the source examples, exercises, and supplied answers.

## Build

Requires Node >=26, npm 11, and Python 3. Python conversion dependencies and pandoc are needed only for reimporting.

```bash
npm ci
npm run start
npm run verify
npm run check
```

The complete site is built into `_build/html`, with search, navigation, and the template’s PWA support. To use the intended GitHub Pages project path locally:

```bash
BASE_URL=/beginningStatistics npm run build
```

## Source and license

Adapted from [Beginning Statistics, v1.0](https://2012books.lardbucket.org/books/beginning-statistics/), preserved by **Andy Schmitz** on December 29, 2012, under [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/). The source requests omission of customary author and publisher attribution; its notice is preserved in [license.md](front/license.md). Source biographical front matter is retained.

See [SOURCES.md](SOURCES.md), [LICENSE](LICENSE), [image credits](image-credits.md), and [figure audit](FIGURE-AUDIT.md). The source instructional diagrams and table scans retain the textbook license; undocumented portraits are replaced with original typographic name cards. Template code remains under [MIT](LICENSE-CODE).

## Repeat the import

Download and extract the [original archive](https://2012books.lardbucket.org/zips/beginning-statistics.zip). SHA-256: `85db542c75ca7543532329829571d59a332068fd6922751c6cde51630431f7eb`.

Install pandoc and `python3 -m pip install -r scripts/requirements-import.txt`, then:

```bash
npm run import:source -- /path/to/beginning-statistics
npm run check
```

The import copies all book content, converts MathML into TeX, rewrites internal references, supplies image alternative text, generates name-card replacements and credits, and updates the table of contents. `source/manifest.json` records coverage, provenance, and SHA-256 checksums. Source HTML is included for traceability. Imports overwrite converted Markdown; editorial changes must be made reproducible in the importer.

## Source limitations

The preserved archive does not include the companion spreadsheets used by “Large Data Set Exercises.” Their prompts remain in the book; those exercises need separately supplied data. Appendix distribution tables are high-resolution raster scans rather than accessible numeric tables. The source has not received a full statistical content audit.

## Layout

- `chapters/`: eleven complete chapters, one file per chapter.
- `front/`: license, author biographies, acknowledgements, dedication, and preface.
- `appendices/`: statistical reference tables at their original scan resolution.
- `images/`: SVG redraws of every diagram (`images/redrawn/`), appendix table scans, two equation images, branding, and replacement name cards.
- `source/`: original combined HTML pages and import manifest.
- `scripts/`: conversion, verification, and PWA setup.
- `.github/`: shared CI, dependency updates, and Pages deployment configuration.

The [GitHub repository](https://github.com/QuadriviumPress/beginningStatistics) publishes the [online textbook](https://quadriviumpress.com/beginningStatistics/) through GitHub Pages. Every push to `main` runs the strict checks before publication. The book is registered in bindery’s catalog and the public QuadriviumPress book listings.
