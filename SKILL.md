---
name: hello-sugar-brand
description: >-
  Apply the Hello Sugar visual brand — colors, typography, logos, and design
  tokens — to any user interface. Use this skill WHENEVER building, designing,
  styling, or restyling a web page, internal tool, dashboard, form, component,
  email template, or any UI for Hello Sugar, even if the user does not say the
  word "brand." If the work will be seen by Hello Sugar staff or customers and
  has any visual surface, pull in this skill so the result looks and feels like
  Hello Sugar. Works alongside frontend/design plugins: this skill supplies the
  brand palette and rules; the plugins handle layout and composition.
---

# Hello Sugar Brand

Hello Sugar ("Braz Wax and Sugar Salon" — Hair Removal · Wax · Sugar · Laser) is
a franchise salon brand. This skill makes any UI you build look like it belongs
to Hello Sugar by giving you the canonical design tokens, fonts, and logos plus
the rules for applying them.

## How this fits with design plugins

This skill is the **constraint layer**, not a replacement for design tooling.
Frontend/design plugins decide layout, composition, spacing rhythm, and overall
craft. This skill fixes the *palette, type, logo usage, and brand rules* they
work within. When both are active: let the design plugin drive structure and
aesthetics, and treat the tokens and rules below as non-negotiable inputs —
brand colors instead of invented ones, Montserrat for UI, the supplied logos,
and the accessibility limits in the reference doc.

## The fastest correct path

The brand lives as **framework-agnostic tokens** so it applies in any stack.
`tokens/tokens.json` is the single source of truth; two consumable outputs are
generated from it.

1. **Any stack (default): CSS variables.** Import `tokens/variables.css` once
   globally, then reference `var(--hs-color-*)`, `var(--hs-font-*)`,
   `var(--hs-radius-*)`, etc. This works in plain HTML/CSS, React, Vue, Svelte,
   server-rendered pages — anything.
2. **Tailwind tools: the preset.** Add `tokens/tailwind-preset.js` to
   `tailwind.config.js` (`presets: [require('./tokens/tailwind-preset.js')]`) and
   use classes like `bg-hs-primary`, `text-hs-text`, `border-hs-border`,
   `rounded-lg`, `shadow-md`.
3. **Fonts.** Import `assets/fonts/fonts.css` once at the app root so the
   `--hs-font-*` families resolve. Montserrat can alternatively be loaded from
   Google Fonts.

Pick the path that matches the tool's stack. Both paths produce identical brand
values because both come from `tokens.json`.

## Core tokens to reach for

Always prefer the **semantic** `--hs-color-*` tokens over the raw
`--hs-brand-*` palette, so intent stays consistent.

- **Backgrounds:** `bg` (cream, page), `surface` (white, cards), `surface-alt`
  (faint warm card alt).
- **Text:** `text` (dark warm ink — all body copy), `text-muted` (secondary),
  `text-subtle` (disabled/decorative). Never use a brand color for body text.
- **Actions:** `primary` (crimson) with `on-primary` (white) for labels;
  `primary-strong` for hover/active; `primary-soft` (blush) for tinted
  badges/backgrounds. Add a `focus` ring on every interactive element.
- **Emphasis:** `accent` (caramel) and `deep` (rose) for secondary emphasis,
  icons, and accent headings.
- **Status:** `success` / `warning` / `danger` / `info` (+ their `-soft`
  variants) for state UI.
- **Shape:** generous radii — the brand reads soft and rounded. Use
  `radius-lg`/`radius-xl` for cards and `radius-pill` for buttons and badges.

## Typography quick rules

- **Montserrat** for everything functional (body, labels, buttons, tables,
  most headings). It's the default UI font.
- **LiebeLotte** (the script) only for one large brand moment per screen — a
  hero title or login header. Never for small text. It is a licensed font;
  verify web-embed rights before public-facing use (internal tools usually fine).
- Set body text in ink at `font-size-base`; reserve crimson and warm colors for
  headings, accents, and chrome.

## Logos

In `assets/logos/`: use **internal/** (no ® mark) for internal tools — the usual
case here — and **external/** (with ®) for customer-facing surfaces. Prefer the
SVG (`internal/hello-sugar-full-color.svg`) where vector works. Pick `horizontal`
for top nav, `stacked` for splash/login, and `drop` (teardrop mark) for icons,
favicons, and tight spaces. Give clear space around it, don't recolor or
distort, and never rebuild the wordmark from fonts.

## Before you ship a UI, check

- Colors come from `--hs-color-*` tokens, not hard-coded hex.
- Body text is ink; crimson/warm colors are used only for emphasis and chrome.
- Interactive elements have a visible `focus` ring and sufficient contrast (see
  reference doc — white-on-crimson is large/UI only).
- The correct logo variant (internal vs external) is used.

## Going deeper

Read `references/brand-guidelines.md` for the full color-role table, exact WCAG
contrast measurements and limits, detailed font roles and licensing, and logo
do/don't rules. See `examples/vanilla.html` (CSS-variables, any stack) and
`examples/StatCard.jsx` (React + Tailwind preset) for working references. To
change the brand, edit `tokens/tokens.json` and run `python tokens/generate.py`
— never hand-edit the generated `variables.css` or `tailwind-preset.js`.
