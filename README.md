# Hello Sugar Brand — Claude Skill

The canonical Hello Sugar visual brand — colors, typography, logos, and design
tokens — packaged as a [Claude Code](https://claude.com/claude-code) skill.

Install it once and Claude automatically applies the brand whenever you ask it
to build or restyle a page, internal tool, dashboard, form, component, or email
template for Hello Sugar. You don't have to say the word "brand."

**This repo is the skill folder.** `SKILL.md` is at the root, so you can clone it
straight into your skills directory.

---

## Install (Claude Code)

### Option A — available in every project (recommended)

```bash
git clone https://github.com/Hello-Brands/hello-sugar-brand-skill.git ~/.claude/skills/hello-sugar-brand
```

Windows PowerShell:

```powershell
git clone https://github.com/Hello-Brands/hello-sugar-brand-skill.git "$env:USERPROFILE\.claude\skills\hello-sugar-brand"
```

### Option B — one project only

From the root of that project:

```bash
git clone https://github.com/Hello-Brands/hello-sugar-brand-skill.git .claude/skills/hello-sugar-brand
```

Commit it if you want everyone on the repo to get it, or add
`.claude/skills/hello-sugar-brand/` to `.gitignore` if you don't.

### Option C — no git

Download the ZIP (**Code → Download ZIP** at the top of this page), unzip it,
and rename the folder to `hello-sugar-brand` inside `~/.claude/skills/`.

The folder name matters — it must be `hello-sugar-brand`, matching the `name:`
in `SKILL.md`.

### Confirm it worked

Start (or restart) Claude Code and run `/skills`. You should see
`hello-sugar-brand` in the list. Then try:

> Build me a small internal dashboard page for tracking location supply orders.

Claude should pull in the skill on its own and come back with cream backgrounds,
crimson actions, Montserrat, and the right logo.

## Updating

```bash
cd ~/.claude/skills/hello-sugar-brand && git pull
```

## Using it without Claude

The tokens are framework-agnostic — you can consume them directly in any
project:

- **Any stack:** import `tokens/variables.css` globally, then use
  `var(--hs-color-primary)`, `var(--hs-font-ui)`, `var(--hs-radius-pill)`, etc.
- **Tailwind:** add `tokens/tailwind-preset.js` to your config —
  `presets: [require('./tokens/tailwind-preset.js')]` — then use `bg-hs-primary`,
  `text-hs-text`, `border-hs-border`.
- **Fonts:** import `assets/fonts/fonts.css` once at the app root.

Working references live in `examples/vanilla.html` (plain CSS variables) and
`examples/StatCard.jsx` (React + Tailwind preset).

## What's in here

| Path | What it is |
| --- | --- |
| `SKILL.md` | The instructions Claude reads — the fast path, core tokens, type and logo rules |
| `tokens/tokens.json` | **Single source of truth** for every brand value |
| `tokens/variables.css` | Generated CSS custom properties (`--hs-*`) |
| `tokens/tailwind-preset.js` | Generated Tailwind preset |
| `tokens/generate.py` | Regenerates the two files above from `tokens.json` |
| `assets/fonts/` | Montserrat, Montserrat Alternates, LiebeLotte, Fifita + `fonts.css` |
| `assets/logos/internal/` | Logos **without** the ® mark — for internal tools |
| `assets/logos/external/` | Logos **with** the ® mark — for customer-facing surfaces |
| `examples/` | A vanilla HTML page and a React/Tailwind component |
| `references/brand-guidelines.md` | Full color-role table, WCAG contrast limits, font licensing, logo do/don't |

## Changing the brand

Edit `tokens/tokens.json`, then run:

```bash
python tokens/generate.py
```

Never hand-edit `variables.css` or `tailwind-preset.js` — they're generated and
your changes will be overwritten. Open a PR so everyone picks the change up on
their next `git pull`.

## A note on the assets

The font files and logos in this repo are licensed and proprietary to Hello
Sugar. Keep this repository private, and check web-embedding rights for
LiebeLotte before shipping it on a public, customer-facing surface — internal
tools are the normal use.
