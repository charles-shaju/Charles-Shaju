#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any


BG = "#0d1117"
FG = "#c9d1d9"
MUTED = "#8b949e"
BORDER = "#30363d"

PALETTE = [
    "#58a6ff",  # blue
    "#f78166",  # salmon
    "#d2a8ff",  # purple
    "#7ee787",  # green
    "#ffa657",  # orange
    "#a5d6ff",  # light blue
]


@dataclass(frozen=True)
class Slice:
    label: str
    value: int
    color: str


def _escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def _request_json(url: str, *, token: str | None) -> tuple[Any, dict[str, str]]:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "readme-assets-generator")
    if token:
        req.add_header("Authorization", f"Bearer {token}")

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return json.loads(body), headers
    except urllib.error.HTTPError as e:
        msg = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} for {url}: {msg[:300]}")


def _next_link(link_header: str | None) -> str | None:
    if not link_header:
        return None
    # Very small Link parser: look for rel="next"
    for part in link_header.split(","):
        part = part.strip()
        if 'rel="next"' not in part:
            continue
        if part.startswith("<") and ">" in part:
            return part[1 : part.index(">")]
    return None


def fetch_language_bytes(username: str, *, token: str | None, max_repos: int = 200) -> dict[str, int]:
    url = f"https://api.github.com/users/{urllib.parse.quote(username)}/repos?per_page=100&sort=updated"

    totals: dict[str, int] = {}
    seen = 0

    while url and seen < max_repos:
        repos, headers = _request_json(url, token=token)
        if not isinstance(repos, list):
            raise RuntimeError("Unexpected GitHub API response for repos")

        for repo in repos:
            if seen >= max_repos:
                break
            if not isinstance(repo, dict):
                continue
            if repo.get("fork") is True:
                continue
            languages_url = repo.get("languages_url")
            if not isinstance(languages_url, str):
                continue

            lang_map, _ = _request_json(languages_url, token=token)
            if isinstance(lang_map, dict):
                for lang, b in lang_map.items():
                    if isinstance(lang, str) and isinstance(b, int) and b > 0:
                        totals[lang] = totals.get(lang, 0) + b

            seen += 1

        url = _next_link(headers.get("link"))

    if not totals:
        raise RuntimeError("No language data found")

    return totals


def _polar(cx: float, cy: float, r: float, angle_deg: float) -> tuple[float, float]:
    rad = math.radians(angle_deg)
    return cx + r * math.cos(rad), cy + r * math.sin(rad)


def _arc_path(cx: float, cy: float, r: float, start_deg: float, end_deg: float) -> str:
    # SVG arc: sweep clockwise by default if sweep-flag=1.
    sx, sy = _polar(cx, cy, r, start_deg)
    ex, ey = _polar(cx, cy, r, end_deg)
    large_arc = 1 if (end_deg - start_deg) % 360 > 180 else 0
    return f"M {sx:.3f} {sy:.3f} A {r:.3f} {r:.3f} 0 {large_arc} 1 {ex:.3f} {ey:.3f}"


def render_donut(slices: list[Slice], *, width: int = 420, height: int = 220) -> str:
    pad = 14
    cx = 120
    cy = 110
    r = 74
    stroke = 18

    total = sum(s.value for s in slices)
    if total <= 0:
        raise RuntimeError("Invalid donut total")

    parts: list[str] = []
    parts.append(
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}' viewBox='0 0 {width} {height}' role='img' aria-label='Top languages'>"
    )
    parts.append(f"<rect x='0' y='0' width='{width}' height='{height}' rx='14' fill='{BG}' stroke='{BORDER}'/>")
    parts.append(
        "<style>"
        f".t{{font:12px -apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;fill:{FG}}}"
        f".m{{fill:{MUTED}}}"
        "</style>"
    )

    # Title
    parts.append(f"<text class='t' x='{pad}' y='{22}'>Tech Stack &amp; Languages</text>")

    # Base ring
    parts.append(
        f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='{BORDER}' stroke-width='{stroke}'/>")

    # Slices start at top (-90deg)
    angle = -90.0
    for s in slices:
        frac = s.value / total
        sweep = frac * 360.0
        start = angle
        end = angle + sweep
        angle = end

        path = _arc_path(cx, cy, r, start, end)
        pct = int(round(frac * 100))
        title = _escape(f"{s.label}: {pct}%")
        parts.append(
            f"<path d='{path}' fill='none' stroke='{s.color}' stroke-width='{stroke}' stroke-linecap='butt'>"
            f"<title>{title}</title>"
            "</path>"
        )

    # Inner cutout
    parts.append(f"<circle cx='{cx}' cy='{cy}' r='{r - stroke / 2 - 8}' fill='{BG}'/>")

    # Center label
    parts.append(f"<text class='t' x='{cx}' y='{cy}' text-anchor='middle' dominant-baseline='middle'>langs</text>")

    # Legend
    lx = 230
    ly = 70
    line_h = 22
    for i, s in enumerate(slices):
        frac = s.value / total
        pct = int(round(frac * 100))
        y = ly + i * line_h
        parts.append(f"<circle cx='{lx}' cy='{y - 4}' r='5' fill='{s.color}'/>")
        parts.append(f"<text class='t' x='{lx + 14}' y='{y}'>{_escape(s.label)}</text>")
        parts.append(f"<text class='t m' x='{width - pad}' y='{y}' text-anchor='end'>{pct}%</text>")

    parts.append(f"<text class='t m' x='{pad}' y='{height - 12}'>Based on public repositories</text>")
    parts.append("</svg>")
    return "".join(parts)


def build_slices(language_bytes: dict[str, int], *, top_n: int = 5) -> list[Slice]:
    items = sorted(language_bytes.items(), key=lambda kv: kv[1], reverse=True)
    top = items[:top_n]
    rest_val = sum(v for _, v in items[top_n:])

    slices: list[Slice] = []
    for idx, (lang, val) in enumerate(top):
        slices.append(Slice(label=lang, value=val, color=PALETTE[idx % len(PALETTE)]))
    if rest_val > 0:
        slices.append(Slice(label="Other", value=rest_val, color=BORDER))
    return slices


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a GitHub-dark donut chart of languages.")
    parser.add_argument("--username", required=True)
    parser.add_argument("--output", default="-")
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")

    language_bytes = fetch_language_bytes(args.username, token=token)
    slices = build_slices(language_bytes, top_n=args.top)
    svg = render_donut(slices)

    if args.output == "-":
        sys.stdout.write(svg)
    else:
        with open(args.output, "w", encoding="utf-8", newline="\n") as f:
            f.write(svg)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
