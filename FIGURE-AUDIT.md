# Figure audit

The 16 top-level source pages contain 145 image slots: 130 instructional diagrams, 13 appendix table scans, and two author photographs. All source slots were inspected in contact sheets. No stock photographs or separately credited third-party images appear among the instructional diagrams and table scans. Their source textbook license is retained.

The two portraits lack separate rights documentation and are replaced with original typographic name cards. Their original image bytes are excluded. `figure-replacements.json` records the original and replacement checksums. Original HTML retains the source references for provenance.

128 diagrams are redrawn as SVG by `scripts/render_figures.py`, using only the Python standard library. Curves are computed from the distributions they depict, and every label, value, and critical point is checked against the source figure and the worked example it illustrates. Student *t* figures stay schematic, as in the source: each *t* value is placed where the drawn bell curve encloses the same tail area. Each SVG has a title and a description, and its figure has a full text alternative. Data plots are computed from the data printed in the text; random illustrations are measured from the source images. Four source labeling errors are corrected (in Figures 2.13, 2.18, and 8.16 and the Example 21 illustration; see `SOURCES.md`). The source rasters of redrawn figures are not shipped; `figure-replacements.json` records their checksums.

The other 15 assets are copied without resizing or recompression, including the high-resolution appendix tables. Figure titles and source identifiers are preserved; alternative text is supplied for every image. Table scans remain raster images, so their numeric cells are not screen-reader-accessible tables. This is a known limitation of this source adaptation.

See [Image credits](image-credits.md) for every slot and `source/manifest.json` for the machine-readable asset ledger. Rendered-content verification checks that all 145 image occurrences survive the build.
