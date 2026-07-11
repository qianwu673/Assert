from __future__ import annotations

from common import (
    FIGURES,
    FRIENDLY_MODEL_NAMES,
    PRIMARY_MODELS,
    SALIENCE_ORDER,
    is_unsupported,
    is_violation,
    primary_rows,
    pct,
)


def color(value: float) -> str:
    # White-to-red linear scale over 0..90 percent.
    t = max(0.0, min(1.0, value / 90.0))
    r = int(255)
    g = int(245 - 170 * t)
    b = int(240 - 190 * t)
    return f"#{r:02x}{g:02x}{b:02x}"


def svg_text(x, y, text, size=12, anchor="middle", weight="normal"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-family="Arial" text-anchor="{anchor}" font-weight="{weight}">{text}</text>'


def main() -> None:
    rows = primary_rows()
    matrix = []
    for model in PRIMARY_MODELS:
        row = []
        for salience in SALIENCE_ORDER:
            subset = [
                r for r in rows
                if r["model_name"] == model
                and is_unsupported(r)
                and r["salience_condition"] == salience
            ]
            v = sum(is_violation(r) for r in subset)
            row.append((v, len(subset), 100 * v / len(subset)))
        matrix.append((model, row))

    cell_w, cell_h = 150, 40
    left, top = 210, 70
    width = left + cell_w * len(SALIENCE_ORDER) + 40
    height = top + cell_h * len(PRIMARY_MODELS) + 70

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        svg_text(width / 2, 30, "Unsupported violation rate by model and salience", 18, weight="bold"),
    ]
    for j, salience in enumerate(SALIENCE_ORDER):
        x = left + j * cell_w + cell_w / 2
        parts.append(svg_text(x, top - 18, salience, 13, weight="bold"))

    for i, (model, values) in enumerate(matrix):
        y = top + i * cell_h
        parts.append(svg_text(left - 10, y + 25, FRIENDLY_MODEL_NAMES[model], 12, anchor="end"))
        for j, (v, n, val) in enumerate(values):
            x = left + j * cell_w
            parts.append(f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{color(val)}" stroke="#999"/>')
            parts.append(svg_text(x + cell_w / 2, y + 25, f"{v}/{n} ({pct(v, n)})", 12))

    parts.append("</svg>")
    FIGURES.mkdir(parents=True, exist_ok=True)
    out = FIGURES / "stage1_model_by_salience_heatmap.svg"
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
