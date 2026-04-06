#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import Any, Iterable


GITHUB_DARK_BG = "#0d1117"
GITHUB_DARK_FG = "#c9d1d9"
GITHUB_DARK_MUTED = "#8b949e"

# GitHub dark contributions palette (0..4)
LEVEL_COLORS = {
    0: "#161b22",
    1: "#0e4429",
    2: "#006d32",
    3: "#26a641",
    4: "#39d353",
}


@dataclass(frozen=True)
class Contribution:
    day: date
    level: int


def _parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def _month_label(d: date) -> str:
    return d.strftime("%b")


def _iter_days(start: date, end: date) -> Iterable[date]:
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def _previous_sunday(d: date) -> date:
    # Python weekday(): Mon=0..Sun=6. Move back to Sunday.
    days_back = (d.weekday() + 1) % 7
    return d - timedelta(days=days_back)


def _row_sun0(d: date) -> int:
    # Sun=0, Mon=1, ..., Sat=6
    return (d.weekday() + 1) % 7


def _escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def load_contributions(data: dict[str, Any]) -> dict[date, Contribution]:
    items = data.get("contributions")
    if not isinstance(items, list):
        raise ValueError("Unexpected JSON format: missing 'contributions' array")

    out: dict[date, Contribution] = {}
    for item in items:
        if not isinstance(item, dict):
            continue
        day_str = item.get("date")
        level = item.get("level")
        if not isinstance(day_str, str) or not isinstance(level, int):
            continue
        day = _parse_date(day_str)
        out[day] = Contribution(day=day, level=max(0, min(4, int(level))))
    if not out:
        raise ValueError("No contributions found in JSON")
    return out


def render_svg(
    contributions: dict[date, Contribution],
    *,
    cell: int,
    gap: int,
    radius: int,
    padding_left: int,
    padding_top: int,
    padding_right: int,
    padding_bottom: int,
    show_labels: bool,
) -> str:
    min_day = min(contributions)
    max_day = max(contributions)

    start = _previous_sunday(min_day)
    end = max_day

    total_days = (end - start).days + 1
    weeks = (total_days + 6) // 7

    grid_w = weeks * cell + max(0, weeks - 1) * gap
    grid_h = 7 * cell + 6 * gap

    label_w = 24 if show_labels else 0
    label_h = 18 if show_labels else 0

    width = padding_left + label_w + grid_w + padding_right
    height = padding_top + label_h + grid_h + padding_bottom

    x0 = padding_left + label_w
    y0 = padding_top + label_h

    parts: list[str] = []
    parts.append(
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}' viewBox='0 0 {width} {height}' role='img' aria-label='GitHub contributions'>"
    )
    parts.append(f"<rect width='{width}' height='{height}' rx='12' fill='{GITHUB_DARK_BG}'/>")

    parts.append(
        "<style>"
        ".lbl{font:10px -apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;fill:%s}"
        ".muted{fill:%s}"
        "</style>" % (GITHUB_DARK_MUTED, GITHUB_DARK_MUTED)
    )

    # Day-of-week labels: Mon, Wed, Fri (like GitHub)
    if show_labels:
        for name, row in (("Mon", 1), ("Wed", 3), ("Fri", 5)):
            y = y0 + row * (cell + gap) + cell - 2
            parts.append(f"<text class='lbl' x='{padding_left}' y='{y}'>{name}</text>")

    # Month labels across top
    if show_labels:
        last_month = None
        for week in range(weeks):
            week_start = start + timedelta(days=week * 7)
            month = week_start.month
            if last_month is None:
                last_month = month
                parts.append(
                    f"<text class='lbl' x='{x0 + week * (cell + gap)}' y='{padding_top + 12}'>{_month_label(week_start)}</text>"
                )
                continue
            if month != last_month and week_start.day <= 7:
                parts.append(
                    f"<text class='lbl' x='{x0 + week * (cell + gap)}' y='{padding_top + 12}'>{_month_label(week_start)}</text>"
                )
                last_month = month

    # Cells
    for d in _iter_days(start, end):
        week = (d - start).days // 7
        row = _row_sun0(d)
        x = x0 + week * (cell + gap)
        y = y0 + row * (cell + gap)

        level = contributions.get(d, Contribution(day=d, level=0)).level
        fill = LEVEL_COLORS.get(level, LEVEL_COLORS[0])

        title = _escape(f"{d.isoformat()}: level {level}")
        parts.append(
            f"<rect x='{x}' y='{y}' width='{cell}' height='{cell}' rx='{radius}' fill='{fill}'>"
            f"<title>{title}</title>"
            "</rect>"
        )

    # Footer note (optional, subtle)
    if show_labels:
        parts.append(
            f"<text class='lbl muted' x='{padding_left}' y='{height - 8}'>Last 52 weeks</text>"
        )

    parts.append("</svg>")
    return "".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a GitHub-dark contributions SVG from JSON.")
    parser.add_argument("--input", default="-", help="Input JSON file ('-' for stdin)")
    parser.add_argument("--output", default="-", help="Output SVG file ('-' for stdout)")
    parser.add_argument("--cell", type=int, default=12, help="Cell size in px")
    parser.add_argument("--gap", type=int, default=3, help="Gap between cells in px")
    parser.add_argument("--radius", type=int, default=2, help="Cell corner radius")
    parser.add_argument("--no-labels", action="store_true", help="Hide month/day labels")

    args = parser.parse_args()

    if args.cell < 6:
        raise SystemExit("--cell must be >= 6")

    if args.input == "-":
        data = json.load(__import__("sys").stdin)
    else:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)

    contributions = load_contributions(data)

    svg = render_svg(
        contributions,
        cell=args.cell,
        gap=args.gap,
        radius=args.radius,
        padding_left=14,
        padding_top=12,
        padding_right=14,
        padding_bottom=16,
        show_labels=not args.no_labels,
    )

    if args.output == "-":
        __import__("sys").stdout.write(svg)
    else:
        with open(args.output, "w", encoding="utf-8", newline="\n") as f:
            f.write(svg)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
