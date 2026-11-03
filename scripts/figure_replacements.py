"""Preserve teaching diagrams and replace undocumented portraits with name cards."""
import hashlib
import html
import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = 'https://2012books.lardbucket.org/books/beginning-statistics/'
CONTENT_LICENSE = 'https://creativecommons.org/licenses/by-nc-sa/3.0/'
PORTRAITS = {
    '43a57aa5174aa48c749d72adc0ecc342': 'Douglas S. Shafer',
    '27273eef185dd7263d7c9f9954725169': 'Zhiyi Zhang',
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def label(value):
    return 'src-' + re.sub(r'[^a-zA-Z0-9-]', '-', value).lower()


def md(node):
    return subprocess.run(['pandoc', '-f', 'html-native_divs-native_spans', '-t', 'markdown+tex_math_dollars-subscript-superscript', '--wrap=none'],
                          input=str(node), text=True, capture_output=True, check=True).stdout.strip()


def prepare_figures(source, entries):
    plans = {}
    slots = []
    for entry in entries:
        for image in entry['body'].select('img'):
            src = image['src']
            key = Path(src).stem
            figure = image.find_parent(class_=lambda c: c and 'figure' in c)
            title = figure.select_one('.title') if figure else None
            paragraph = image.find_previous('p')
            context = title.get_text(' ', strip=True) if title else paragraph.get_text(' ', strip=True) if paragraph else entry['title']
            # Resolve all descriptions before conversion tokens replace context.
            image['alt'] = image.get('alt') or ('Statistical diagram: ' + context[:500])
            if key in PORTRAITS:
                name = PORTRAITS[key]
                slug = re.sub(r'[^a-z]+', '-', name.lower()).strip('-')
                dest = ROOT / 'images' / 'replacements' / (slug + '.svg')
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 180" role="img" aria-labelledby="title">
<title id="title">{html.escape(name)} — author name card</title>
<rect width="640" height="180" rx="16" fill="#edf3f9"/>
<path d="M38 40v100h80" fill="none" stroke="#315c8c" stroke-width="4"/>
<path d="M44 130q30-170 68 0" fill="none" stroke="#315c8c" stroke-width="4"/>
<text x="155" y="98" font-family="sans-serif" font-size="32" fill="#173451">{html.escape(name)}</text>
<text x="155" y="132" font-family="sans-serif" font-size="18" fill="#315c8c">Source-edition author</text>
</svg>
''')
                plans[key] = {'original_asset': src, 'original_sha256': sha(source / src),
                              'path': str(dest.relative_to(ROOT)), 'sha256': sha(dest),
                              'alt': f'Author name card for {name}; typographic replacement for the source portrait.',
                              'credit': 'QuadriviumPress', 'license': 'CC BY-NC-SA 3.0',
                              'license_url': CONTENT_LICENSE, 'source': 'scripts/figure_replacements.py',
                              'page': entry['file'], 'title': name}
            elif figure and re.search(r'Thinkstock|Getty|permission|copyright|©', figure.get_text(), re.I):
                raise ValueError(f'Unreviewed image credit: {src}')
            slots.append({'page': entry['file'], 'source': src, 'title': context,
                          'action': 'Original name card replaces undocumented portrait' if key in PORTRAITS else 'Retain source instructional artwork'})
    if set(plans) != set(PORTRAITS):
        raise ValueError('Source portrait inventory changed')
    (ROOT / 'figure-replacements.json').write_text(json.dumps({'entries': plans}, indent=2, ensure_ascii=False) + '\n')
    credits = ['# Image credits\n',
               'All 143 source instructional diagrams and statistical table scans are retained under the textbook’s '
               '[CC BY-NC-SA 3.0 license](https://creativecommons.org/licenses/by-nc-sa/3.0/). '
               'The two source portraits have been replaced by original QuadriviumPress typographic name cards, '
               'released under the same license. These cards do not portray the authors. '
               'Every asset’s source, description, license, and checksum is recorded in `source/manifest.json`.\n',
               '## Figures by chapter\n', '| Page | Source artwork | Treatment |\n| --- | --- | --- |']
    for slot in slots:
        title = slot['title'].replace('|', '\\|').replace('\n', ' ')
        credits.append(f'| [{Path(slot["page"]).stem}]({slot["page"]}) | {title} (`{Path(slot["source"]).stem[:8]}`) | {slot["action"]} |')
    (ROOT / 'image-credits.md').write_text('\n'.join(credits) + '\n')
    (ROOT / 'FIGURE-AUDIT.md').write_text('''# Figure audit

The 16 top-level source pages contain 145 image slots: 130 instructional diagrams, 13 appendix table scans, and two author photographs. All source slots were inspected in contact sheets. No stock photographs or separately credited third-party images appear among the instructional diagrams and table scans. Their source textbook license is retained.

The two portraits lack separate rights documentation and are replaced with original typographic name cards. Their original image bytes are excluded. `figure-replacements.json` records the original and replacement checksums. Original HTML retains the source references for provenance.

All 143 retained assets are copied without resizing or recompression, including the high-resolution appendix tables. Figure titles and source identifiers are preserved; alternative text is supplied for every image. Table scans remain raster images, so their numeric cells are not screen-reader-accessible tables. This is a known limitation of this source adaptation.

See [Image credits](image-credits.md) for every slot and `source/manifest.json` for the machine-readable asset ledger. Rendered-content verification checks that all 145 image occurrences survive the build.
''')
    return plans


def asset_record(image, source, entry, ledger, manifest):
    src = image['src']
    key = Path(src).stem
    if key in ledger:
        record = dict(ledger[key])
    else:
        original = (source / src).resolve()
        if not original.is_relative_to(source.resolve()):
            raise ValueError(f'Unsafe image path: {src}')
        dest = ROOT / 'images' / src
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(original, dest)
        record = {'path': str(dest.relative_to(ROOT)), 'sha256': sha(dest), 'source_sha256': sha(original),
                  'alt': image['alt'], 'credit': 'Source textbook instructional artwork',
                  'license': 'CC BY-NC-SA 3.0', 'license_url': CONTENT_LICENSE,
                  'source': UPSTREAM + entry['source']}
    manifest['assets'][record['path']] = record
    return record


def figure_node(figure, source, entry, ledger, manifest):
    images = figure.select('img')
    if not images:
        return md(figure)
    title = figure.select_one('.title')
    caption = md(title) if title else ''
    # A figure title is a paragraph, not a heading in the MyST caption.
    caption = re.sub(r'^#+\s*', '', caption)
    parts = []
    for i, image in enumerate(images):
        record = asset_record(image, source, entry, ledger, manifest)
        text = f'``````{{figure}} /{record["path"]}\n:alt: {record["alt"]}\n'
        if figure.get('id') and i == 0:
            text += f':name: {label(figure["id"])}\n'
        text += '\n' + caption
        if Path(image['src']).stem in ledger:
            text += f'\n\nOriginal typographic name card by QuadriviumPress; [CC BY-NC-SA 3.0]({CONTENT_LICENSE}).'
        text += '\n``````'
        parts.append(text)
    for paragraph in figure.find_all('p', recursive=False):
        if paragraph != title and not paragraph.find('img'):
            parts.append(md(paragraph))
    return '\n\n'.join(parts)
