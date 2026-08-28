# Hello Sugar — Brand Guidelines (reference)

Detailed reference for applying the Hello Sugar brand. The SKILL.md covers the
day-to-day workflow; read this when you need the reasoning behind a token, exact
color roles, accessibility limits, or logo/font usage rules.

## The palette and what each color is for

Nine brand colors come from the official palette. They are exposed raw as
`--hs-brand-*` but you should almost always use the **semantic** `--hs-color-*`
tokens instead, so intent stays consistent and the palette can shift without a
find-and-replace.

| Brand color | Hex | Role |
|---|---|---|
| Crimson | `#ED1845` | The signature. Primary actions, key brand moments, the "Sugar" script. |
| Blush | `#F7DCDA` | Soft tinted backgrounds, badges, primary-soft surfaces. |
| Rose | `#AD4C52` | Deep accent — text/icons on light, secondary emphasis. |
| Sand | `#E2CCB9` | Warm neutral fill, accent-soft surfaces. |
| Tan | `#D3AD90` | Warm neutral, decorative. |
| Caramel | `#BB8265` | Secondary/accent — the "Hello" word color. |
| Taupe | `#8F7067` | Muted/secondary text on light surfaces. |
| Mauve | `#CBA499` | Subtle text, disabled states, strong borders. |
| Cream | `#EEE2DA` | The default app background. |

### Semantic mapping (use these)

- **primary / primary-strong / primary-soft / on-primary** — crimson system.
  `primary-strong` (`#C9143B`) is the hover/active shade; `on-primary` is white.
- **accent / accent-soft** — caramel + sand, for secondary emphasis.
- **deep** — rose, for accent text and icons on light backgrounds.
- **bg / surface / surface-alt** — cream page, white cards, faint warm card alt.
- **border / border-strong** — derived warm neutrals.
- **text / text-muted / text-subtle** — a derived dark warm ink (`#1F1917`),
  then taupe, then mauve.
- **success / warning / danger / info** — *additions*. The official palette has
  no green, amber, or blue, so these are harmonized to the warm world for status
  UI. Note that brand crimson is itself red, so `danger` uses a distinct deeper
  red (`#C0142F`) to avoid colliding with primary. Treat these as starting points
  and adjust if Hello Sugar later defines official status colors.

## Accessibility — the rules that actually matter here

The brand reds and warm neutrals are mid-luminance, so contrast is the main
trap. Measured WCAG ratios:

- **White on crimson ≈ 4.4:1** — passes AA for UI components and large text
  (≥18px or ≥14px bold). Just under the 4.5 threshold for small body text, so
  keep button labels ≥16px and medium/semibold weight. Don't set tiny white text
  on crimson.
- **Crimson on white ≈ 4.4:1 / on cream ≈ 3.4:1** — large text and UI only.
  **Never use crimson for body copy.** Headings and accents only.
- **Ink `#1F1917` on cream ≈ 13.7:1, on white ≈ 17.4:1** — the default for all
  body text. Always safe.
- **Taupe on white ≈ 4.5:1, on cream ≈ 3.5:1** — fine for secondary text,
  preferably on white; treat as large/secondary on cream.
- **Rose on cream ≈ 4.2:1** — large text / UI accents, not body.

Rule of thumb: **ink for reading, crimson and warm colors for emphasis and
chrome.** Always pair an interactive color with a visible focus ring
(`--hs-color-focus`).

## Typography roles

- **Montserrat** — the UI workhorse. Everything functional: body, labels,
  buttons, table data, headings in dense tools. Weights available: 300 / 400 /
  500 / 600 / 700. Open-source (SIL OFL), safe to self-host or load from Google
  Fonts.
- **LiebeLotte** — the brand script (the "Sugar" wordmark style). Use only for
  large brand moments: a hero title, a splash, a login screen. Never for body,
  labels, or anything small — it's a display face and hurts legibility at small
  sizes. **Licensing:** LiebeLotte is a commercial font; confirm your web-embed
  license before shipping it on public-facing surfaces. Internal tools are
  usually fine, but verify.
- **Fifita** — a free secondary display option, alternative to LiebeLotte for
  display headers.
- **Montserrat Alternates** — occasional display alt with rounder glyphs.

In practice most internal tools should be Montserrat top to bottom, reserving the
display family for one branded header element so tools feel like Hello Sugar
without becoming hard to read.

## Logo usage

Assets live in `assets/logos/`, split into:

- **internal/** — versions **without** the ® mark. Use these for internal tools
  (the common case here). Includes a scalable SVG (`hello-sugar-full-color.svg`)
  — prefer it wherever vector works.
- **external/** — versions **with** the ® mark. Use for anything customer- or
  public-facing.

Variants in each: `stacked` (Hello over Sugar), `horizontal` (single line, good
for top nav bars), `drop` (the teardrop container mark, good for app icons,
favicons, and avatar/badge spots), plus color / white / black.

Do:
- Give the logo clear space (at least the height of the "H" on all sides).
- Use white/black variants on busy or colored backgrounds; color on light/cream.
- Use the drop mark where space is tight (sidebars, icons, tabs).

Don't:
- Recolor, stretch, rotate, add effects, or place color logo on low-contrast
  backgrounds.
- Reconstruct the wordmark from fonts — always use the supplied asset.

## Regenerating tokens

`tokens/tokens.json` is the only source of truth. After editing it, run
`python tokens/generate.py` to rewrite `variables.css` and `tailwind-preset.js`.
Never hand-edit the generated files. If the team later wants more output formats
(SCSS, JS exports, iOS/Android), Style Dictionary can consume the same JSON.
