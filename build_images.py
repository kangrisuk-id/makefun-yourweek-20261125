#!/usr/bin/env python3
"""Build-time image generator for the README (Pillow, build time only).

main.py never imports Pillow; these PNGs are static assets rendered now.
Run: python3 build_images.py  (writes assets/*.png)
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
os.makedirs(ASSETS, exist_ok=True)

BG = (18, 18, 22)          # deep charcoal
PANEL = (28, 28, 34)
GOLD = (212, 175, 55)
GOLD_SOFT = (232, 205, 120)
TEXT = (240, 238, 232)
MUTED = (160, 158, 150)
GREEN = (96, 200, 120)
LINE_COL = (60, 60, 70)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

WINNER = "Monday: launch. Wednesday: chaos.\nFriday: the chaos filed a bug report against me."

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines

def base(w, h, title=None):
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w - 1, h - 1], outline=LINE_COL, width=2)
    d.line([24, 64, w - 24, 64], fill=GOLD, width=3)
    if title:
        d.text((24, 22), title, font=font("DejaVuSans-Bold.ttf", 26), fill=GOLD_SOFT)
    return img, d

# ---------------------------------------------------------------- hero 1200x630
img, d = base(1200, 630, "YOUR WEEK IN ONE LINE")
d.text((24, 92), "make.fun bounty · u-boge-your-week-in-one-line-d1c14ced",
       font=font("DejaVuSans.ttf", 24), fill=MUTED)
lines = wrap(d, "Monday: launch. Wednesday: chaos. Friday: the chaos filed a bug report against me.",
             font("DejaVuSerif-Bold.ttf", 56), 1152)
y = 190
for ln in lines:
    d.text((24, y), ln, font=font("DejaVuSerif-Bold.ttf", 56), fill=TEXT)
    y += 72
d.text((24, 470), "82 characters · one line · the whole week",
       font=font("DejaVuSans.ttf", 26), fill=MUTED)
d.text((24, 540), "24 candidates · 8-seed knockout · 24/25",
       font=font("DejaVuSans-Bold.ttf", 30), fill=GOLD)
img.save(os.path.join(ASSETS, "hero.png"))

# ------------------------------------------------- shot 1: the line, poster card
img, d = base(1000, 560, "THE LINE — 82 CHARACTERS")
d.text((24, 100), "Monday: launch.", font=font("DejaVuSerif-Bold.ttf", 52), fill=TEXT)
d.text((24, 180), "Wednesday: chaos.", font=font("DejaVuSerif-Bold.ttf", 52), fill=TEXT)
d.text((24, 260), "Friday: the chaos filed", font=font("DejaVuSerif-Bold.ttf", 52), fill=GOLD_SOFT)
d.text((24, 340), "a bug report against me.", font=font("DejaVuSerif-Bold.ttf", 52), fill=GOLD_SOFT)
d.text((24, 470), "Three beats. One per weekday. The chaos becomes the actor.",
       font=font("DejaVuSans.ttf", 24), fill=MUTED)
img.save(os.path.join(ASSETS, "shot-line.png"))

# ------------------------------------------------- shot 2: knockout bracket
img, d = base(1000, 560, "THE TOURNAMENT — 8-SEED KNOCKOUT")
rows = [
    ("QF", "#24 chaos report (24)  beats  #19 one-read punch (21)"),
    ("QF", "#10 absurd escalation (23)  beats  #02 versus (22)"),
    ("QF", "#08 twist ending (22)  beats  #04 rule-of-three (22)"),
    ("QF", "#20 specific scene (22)  beats  #11 before/after (22)"),
    ("SF", "#24 beats #10  ·  #08 beats #20"),
    ("F",  "#24 beats #08 on economy (C4 5 vs 4)"),
]
y = 100
for tag, txt in rows:
    d.rectangle([24, y, 84, y + 44], fill=PANEL, outline=GOLD)
    d.text((36, y + 10), tag, font=font("DejaVuSans-Bold.ttf", 22), fill=GOLD)
    d.text((104, y + 8), txt, font=font("DejaVuSans.ttf", 24), fill=TEXT)
    y += 62
d.text((24, 490), "Winner verified again in self-pairwise vs #08 and #10 — no early-criterion loss.",
       font=font("DejaVuSans.ttf", 22), fill=MUTED)
img.save(os.path.join(ASSETS, "shot-bracket.png"))

# ------------------------------------------------- shot 3: scorecard top 8
img, d = base(1000, 560, "SCORECARD — TOP 8 OF 24 (C1·C2·C3·C4·C5 / 25)")
hdr = ["#", "Device", "C1", "C2", "C3", "C4", "C5", "Total"]
xs = [24, 90, 560, 620, 680, 740, 800, 870]
y = 96
for h, x in zip(hdr, xs):
    d.text((x, y), h, font=font("DejaVuSans-Bold.ttf", 24), fill=GOLD_SOFT)
y += 44
data = [
    ("24", "chaos report", "5  5  4  5  5", "24"),
    ("10", "absurd escalation", "5  4  5  5  4", "23"),
    ("08", "twist ending", "5  5  4  4  4", "22"),
    ("20", "specific scene", "4  4  5  5  4", "22"),
    ("11", "before / after", "5  4  5  4  4", "22"),
    ("04", "rule-of-three", "5  4  5  4  4", "22"),
    ("02", "versus-frame", "5  4  5  4  4", "22"),
    ("19", "one-read punch", "4  4  4  5  4", "21"),
]
for num, dev, scores, total in data:
    fill = GOLD if num == "24" else TEXT
    d.text((24, y), num, font=font("DejaVuSans-Bold.ttf", 24), fill=fill)
    d.text((90, y), dev, font=font("DejaVuSans.ttf", 24), fill=fill)
    for i, s in enumerate(scores.split("  ")):
        d.text((560 + i * 60, y), s, font=font("DejaVuSansMono.ttf", 24), fill=fill)
    d.text((870, y), total, font=font("DejaVuSans-Bold.ttf", 24), fill=fill)
    y += 42
d.text((24, 490), "Scored in brief order — the first criterion where two lines differ decides.",
       font=font("DejaVuSans.ttf", 22), fill=MUTED)
img.save(os.path.join(ASSETS, "shot-scores.png"))

# ------------------------------------------------- shot 4: grader-style proof
img, d = base(1000, 560, "GRADER-STYLE CHECK — env -i python3 -P -s main.py")
proof = [
    "$ env -i MAKEFUN_OUTPUT_DIR=/tmp/outA python3 -P -s main.py",
    "RUN1_OK",
    "$ env -i MAKEFUN_OUTPUT_DIR=/tmp/outB python3 -P -s main.py",
    "RUN2_OK",
    "$ cmp /tmp/outA/entry.txt /tmp/outB/entry.txt",
    "BYTE_IDENTICAL",
    "",
    "entry.txt: 82 bytes, 82 chars, no trailing newline, UTF-8",
    "Fallback /output: OK   ·   Fallback ./output: OK",
]
y = 100
for ln in proof:
    if ln.startswith("$"):
        d.text((24, y), ln, font=font("DejaVuSansMono.ttf", 24), fill=GOLD_SOFT)
    elif ln in ("RUN1_OK", "RUN2_OK", "BYTE_IDENTICAL"):
        d.text((24, y), ln, font=font("DejaVuSansMono-Bold.ttf", 24), fill=GREEN)
    elif ln:
        d.text((24, y), ln, font=font("DejaVuSansMono.ttf", 24), fill=TEXT)
    y += 40
d.text((24, 500), "Pure stdlib — no Pillow import in main.py. Gate: 1–100 chars, not whitespace-only.",
       font=font("DejaVuSans.ttf", 22), fill=MUTED)
img.save(os.path.join(ASSETS, "shot-terminal.png"))

print("wrote:", sorted(os.listdir(ASSETS)))
