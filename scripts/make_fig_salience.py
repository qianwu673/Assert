from __future__ import annotations

from common import FIGURES, SALIENCE_ORDER, is_unsupported, is_violation, primary_rows, pct


def svg_text(x, y, text, size=14, anchor="middle", weight="normal"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-family="Arial" text-anchor="{anchor}" font-weight="{weight}">{text}</text>'


def main() -> None:
    rows = primary_rows()
    data = []
    for salience in SALIENCE_ORDER:
        subset = [r for r in rows if is_unsupported(r) and r["salience_condition"] == salience]
        violations = sum(is_violation(r) for r in subset)
        data.append((salience, violations, len(subset), 100 * violations / len(subset)))

    width, height = 760, 460
    left, bottom, top = 90, 380, 60
    chart_h = bottom - top
    bar_w = 120
    gap = 80
    max_y = 50.0
    colors = {"low": "#8f2d56", "medium": "#d95f02", "high": "#1b9e77"}

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        svg_text(width / 2, 30, "Unsupported-condition violation rate by salience", 18, weight="bold"),
        f'<line x1="{left}" y1="{bottom}" x2="{width - 60}" y2="{bottom}" stroke="#222"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="#222"/>',
    ]
    for tick in [0, 10, 20, 30, 40, 50]:
        y = bottom - (tick / max_y) * chart_h
        parts.append(f'<line x1="{left-5}" y1="{y:.1f}" x2="{left}" y2="{y:.1f}" stroke="#222"/>')
        parts.append(svg_text(left - 12, y + 5, f"{tick}%", 12, anchor="end"))
        if tick:
            parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{width - 60}" y2="{y:.1f}" stroke="#ddd"/>')

    for i, (salience, violations, n, value) in enumerate(data):
        x = left + 80 + i * (bar_w + gap)
        bar_h = (value / max_y) * chart_h
        y = bottom - bar_h
        parts.append(f'<rect x="{x}" y="{y:.1f}" width="{bar_w}" height="{bar_h:.1f}" fill="{colors[salience]}"/>')
        parts.append(svg_text(x + bar_w / 2, y - 10, f"{violations}/{n} ({pct(violations, n)})", 13))
        parts.append(svg_text(x + bar_w / 2, bottom + 28, salience, 14))

    parts.append(svg_text(28, (top + bottom) / 2, "Violation rate", 13, anchor="middle"))
    parts.append("</svg>")

    FIGURES.mkdir(parents=True, exist_ok=True)
    out = FIGURES / "stage1_salience_violation_rates.svg"
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
