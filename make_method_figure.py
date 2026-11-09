#!/usr/bin/env python3
"""Create the balanced-only workflow figure used by the course manuscript."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

fig, ax = plt.subplots(figsize=(11, 4.4))
ax.set_xlim(0, 11)
ax.set_ylim(0, 4.4)
ax.axis("off")

boxes = [
    (0.35, 1.75, 2.9, 1.55, "Controlled perturbations", "6,928 grouped cells\nDose + task + dtype + role\nEvent counts / trials", "#3478b8"),
    (4.05, 1.75, 2.9, 1.55, "Fit and freeze models", "KIP Random Forest\n11 diverse comparisons\nTrain only on perturbations", "#16877a"),
    (7.75, 1.75, 2.9, 1.55, "Balanced replacement\ntest", "2,739 replacement records\n21 budget pairs; 5 repeats\n500 positive + 500 negative", "#c27a22"),
]
for x, y, w, h, title, body, color in boxes:
    patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.08",
                           linewidth=1.8, edgecolor=color, facecolor="white")
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h - 0.22, title, fontsize=10.5, fontweight="bold", color=color,
            va="top", ha="center", linespacing=1.2)
    ax.text(x + 0.15, y + h - 0.78, body, fontsize=8.8, color="#30343b", va="top", linespacing=1.5)

for start, end in [((3.29, 2.53), (3.98, 2.53)), ((6.99, 2.53), (7.68, 2.53))]:
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=16,
                                 linewidth=1.8, color="#52677b"))

ax.text(5.5, 0.95,
        "Save feature-only predictions first; open replacement labels only for balanced scoring.",
        ha="center", va="center", fontsize=10.5, color="#35445a")
ax.text(5.5, 0.48,
        "All formal paper metrics use the same balanced draw manifest.",
        ha="center", va="center", fontsize=10.5, color="#35445a", fontweight="bold")
fig.savefig(OUT / "method-overview.png", dpi=220, bbox_inches="tight")
fig.savefig(OUT / "method-overview.pdf", bbox_inches="tight")
plt.close(fig)
