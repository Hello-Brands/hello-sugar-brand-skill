#!/usr/bin/env python3
"""
Generate framework-agnostic outputs from the canonical token source.

    python generate.py

Reads  tokens.json
Writes variables.css      (CSS custom properties — works in any stack)
       tailwind-preset.js  (Tailwind theme preset for Tailwind tools)

tokens.json is the single source of truth. Never hand-edit the generated
files; change tokens.json and re-run this script.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Which token groups become CSS variables, and their variable prefix.
GROUPS = [
    ("brand",       "hs-brand"),
    ("color",       "hs-color"),
    ("font",        "hs-font"),
    ("font-weight", "hs-font-weight"),
    ("font-size",   "hs-font-size"),
    ("line-height", "hs-leading"),
    ("radius",      "hs-radius"),
    ("space",       "hs-space"),
    ("shadow",      "hs-shadow"),
]


def load():
    with open(os.path.join(HERE, "tokens.json"), encoding="utf-8") as f:
        return json.load(f)


def write_css(tokens):
    lines = [
        "/* AUTO-GENERATED from tokens.json by generate.py — do not edit by hand. */",
        ":root {",
    ]
    for group, prefix in GROUPS:
        lines.append(f"  /* {group} */")
        for key, value in tokens[group].items():
            lines.append(f"  --{prefix}-{key}: {value};")
        lines.append("")
    lines.append("}")
    out = os.path.join(HERE, "variables.css")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    return out


def write_tailwind(tokens):
    c = tokens["color"]
    fz = tokens["font-size"]
    rad = tokens["radius"]
    sp = tokens["space"]
    sh = tokens["shadow"]

    def block(d):
        return "".join(f'        "{k}": "{v}",\n' for k, v in d.items())

    js = f"""// AUTO-GENERATED from tokens.json by generate.py — do not edit by hand.
// Usage:  module.exports = {{ presets: [require('./tokens/tailwind-preset.js')] }}
module.exports = {{
  theme: {{
    extend: {{
      colors: {{
        "hs": {{
{block(c)}        }},
      }},
      fontFamily: {{
        sans: [{tokens['font']['sans']!r}],
        display: [{tokens['font']['display']!r}],
        alt: [{tokens['font']['alt']!r}],
      }},
      fontSize: {{
{block(fz)}      }},
      borderRadius: {{
{block(rad)}      }},
      spacing: {{
{block(sp)}      }},
      boxShadow: {{
{block(sh)}      }},
    }},
  }},
}};
"""
    out = os.path.join(HERE, "tailwind-preset.js")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(js)
    return out


def main():
    tokens = load()
    css = write_css(tokens)
    tw = write_tailwind(tokens)
    print("Wrote", os.path.basename(css))
    print("Wrote", os.path.basename(tw))


if __name__ == "__main__":
    main()
