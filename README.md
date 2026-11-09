# CSCI 5150 course project paper

This directory is the Overleaf-ready paper source for the course project. The narrative and all reported numbers are tied to the completed experiment snapshot in `../results/paper_protocol_20261109_v3/`.

- `main.tex`: canonical manuscript entry point, using the official NeurIPS 2025 style file in `neurips_2025.sty`.
- `references.bib`: verified bibliography, including the supplied anonymous Kernel-Correctness manuscript as the protocol source.
- `figures/`: method overview, model comparison, and budget-sensitivity figures in PDF and PNG form.

The implementation uses scikit-learn and CatBoost; the grouped MLP comparison additionally requires PyTorch. Install the Python dependencies from the project package before re-running the model matrix.

KIP Random Forest is the primary method. The eleven comparisons span prevalence, dose-only isotonic regression, Ridge, softmax spline logistic regression, RBF-SVR, weighted KNN, a grouped MLP, a depth-2 decision tree, ExtraTrees, HistGradientBoosting, and CatBoost. KARE is excluded from the main comparison. All formal tables and figures use the same balanced replacement test draws.

Compile locally with:

```bash
mkdir -p build
tectonic --outdir build main.tex
```

The current draft is checked against the course limit of nine pages including references. The paper's formal results all use the balanced test set; natural-distribution metrics remain supplemental diagnostics in the experiment package.
