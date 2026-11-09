# CSCI 5150 course project paper

This directory is the Overleaf-ready paper source for the course project. The narrative and all reported numbers are tied to the completed experiment snapshot in `../results/paper_protocol_20261108_v4/`.

- `main.tex`: canonical manuscript entry point, using the official NeurIPS 2025 style file in `neurips_2025.sty`.
- `references.bib`: verified bibliography, including the supplied anonymous Kernel-Correctness manuscript as the protocol source.
- `figures/`: method overview, model comparison, and budget-sensitivity figures in PDF and PNG form.

Compile locally with:

```bash
mkdir -p build
tectonic --outdir build main.tex
```

The current draft compiles to eight pages. The paper reports balanced screening and natural-distribution grouped-binomial loss separately because they answer different evaluation questions.
