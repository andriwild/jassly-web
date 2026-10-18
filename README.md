# jassly.ch

Landing page, help, privacy policy, terms and imprint of the Jassly app. Plain HTML and CSS, served by GitHub Pages from `main`.

## Editing

The pages live in `src/pages/`, the shared head, header and footer in `src/layout.html` and `src/partials/`. After a change, build and commit the generated files with the sources:

```bash
python3 build.py              # writes index.html, hilfe/index.html, ...
python3 -m http.server 8000   # preview on http://localhost:8000
```

Never edit the generated HTML in the root or the page folders by hand; `build.py` overwrites it.

## Images

- `assets/img/screens/`: iPhone screenshots in Apple's device frame. They are taken on the iOS simulator with `tool/showcase` in the app repository and framed with mokkr (preset `presets/jassly-website.json`), then copied here without the number prefix.
- `assets/img/badges/`: the official store badges in German, unmodified. Apple's from the [App Store marketing tools](https://toolbox.marketingtools.apple.com/app-store/), Google's from the [Google Play badge page](https://play.google.com/intl/en_us/badges/) (transparent margin trimmed). Both are equally tall, as Google asks.
- `assets/img/og.jpg`: the preview when the link is shared, a screenshot of `src/og-image.html` at 1200×630.
- `assets/img/table.jpg`: one of our own photos of a Jass table, behind the closing call to action.

## When the app is in the stores

In `src/partials/badges.html`, turn each `<span class="badge">` into an `<a class="badge" href="…">` with the store link, drop "bald verfügbar" from the labels and remove the `store-note` line. Then build.

## Testimonials

`src/partials/testimonials.html` holds the section, with placeholders. Only real quotes, with permission of the people quoted. Fill it in and add `{{> testimonials}}` to `src/pages/index.html`, between the perks and the prices.
