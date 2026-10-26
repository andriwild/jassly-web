#!/usr/bin/env python3
"""Builds the site: wraps every page in src/pages in src/layout.html.

Each page starts with a comment holding its title and description:

    <!--
    title: Hilfe – Jassly
    description: Antworten zu Jassly.
    -->

`{{> name}}` includes src/partials/name.html, in pages and in the layout.
src/pages/hilfe.html becomes hilfe/index.html; index.html and 404.html keep
their names. sitemap.xml lists every page but 404.html. Python 3 standard
library only.
"""

import pathlib
import re

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / 'src'
SITE = 'https://jassly.ch'
FLAT = {'index', '404'}

META = re.compile(r'\A<!--\n(.*?)\n-->\n', re.S)
INCLUDE = re.compile(r'\{\{> ([\w-]+)\}\}')


def include(text):
    return INCLUDE.sub(
        lambda m: include((SRC / 'partials' / f'{m[1]}.html').read_text().strip()),
        text,
    )


def build(page, layout):
    source = page.read_text()
    meta = META.match(source)
    if not meta:
        raise SystemExit(f'{page.name}: missing title/description comment')
    fields = dict(line.split(': ', 1) for line in meta[1].splitlines())
    html = (layout
            .replace('{{title}}', fields['title'])
            .replace('{{description}}', fields['description'])
            .replace('{{content}}', include(source[meta.end():].strip())))
    name = page.stem
    target = ROOT / (f'{name}.html' if name in FLAT else f'{name}/index.html')
    target.parent.mkdir(exist_ok=True)
    target.write_text(html)
    return target.relative_to(ROOT)


def sitemap(targets):
    urls = ''.join(
        f'  <url><loc>{SITE}/{t.as_posix().removesuffix("index.html")}</loc></url>\n'
        for t in targets if t.name == 'index.html'
    )
    target = ROOT / 'sitemap.xml'
    target.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'{urls}</urlset>\n'
    )
    return target.relative_to(ROOT)


def main():
    layout = include((SRC / 'layout.html').read_text())
    targets = [build(page, layout) for page in sorted((SRC / 'pages').glob('*.html'))]
    targets.append(sitemap(targets))
    for target in targets:
        print(target)


if __name__ == '__main__':
    main()
