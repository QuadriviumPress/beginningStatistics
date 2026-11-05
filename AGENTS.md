# AGENTS.md

## Standard

Follow the [QuadriviumPress MyST baseline](https://github.com/QuadriviumPress/bindery/blob/main/doc/myst-baseline.md) and [presentation skill](https://github.com/QuadriviumPress/bindery/blob/main/skills/quadrivium-myst-presentation/SKILL.md). Seeded from `opiniatedMystmdBookTemplate`; conversion adapted from the chemistry editions.

## Commands

```bash
npm ci
npm run start
npm run verify
npm run build
npm run check
npm run import:source -- /path/to/beginning-statistics
```

## Intentional differences

- Eleven combined chapters live in `chapters/ch-NN-slug.md`, four front pages in `front/`, and the statistical reference appendix in `appendices/`.
- `import:source` requires Python 3, Beautiful Soup, PyYAML, and pandoc. Builds and verifiers use Node and the Python standard library.
- Source HTML, checksums, counts, local assets, and provenance are recorded in `source/manifest.json`. Only combined chapters are archived; section URLs resolve to their local chapter targets.
- `verify` checks source coverage, links, figures, and checksums. `build` and `check` also verify rendered table, image, equation, and list-item coverage and run PWA setup.
- Source numbering is literal, so automatic numbering is disabled. All mathematical content is converted from MathML to TeX.
- Source author photographs are replaced with original typographic name cards. All 128 diagrams are redrawn as accessible SVG by `scripts/render_figures.py` (`images/redrawn/`); the appendix table scans and two equation images are retained at their original resolution. Their rights and hashes are recorded in the manifest and image credits.
- The textbook retains CC BY-NC-SA 3.0; template code retains MIT in `LICENSE-CODE`.
- Imports regenerate Markdown. Preserve editorial corrections in the importer with source-drift checks and document them in `SOURCES.md`.

## Presentation gap

Learning objectives and key takeaways use MyST callouts, and worked examples use admonitions. Source questions and answer lists retain their numbering, including deliberately empty even-numbered answer slots. Answer groups are dropdowns. This preserves the source pedagogy; newly authored exercises should use the standard exercise/solution directives. Appendix probability tables retain their original high-resolution scans and descriptive alternative text.
