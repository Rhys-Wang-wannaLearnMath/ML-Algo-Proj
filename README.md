# CSCI 5150 course project paper

This directory is the Overleaf-ready paper source for the course project. The narrative and all reported numbers are tied to the completed experiment snapshot in `../results/paper_protocol_20261109_v3/`.

- `main.tex`: canonical manuscript entry point, using the official NeurIPS 2025 style file in `neurips_2025.sty`.
- `references.bib`: verified bibliography, including the supplied anonymous Kernel-Correctness manuscript as the protocol source.
- `figures/`: method overview, model comparison, and budget-sensitivity figures in PDF and PNG form.

The implementation uses scikit-learn and CatBoost; the grouped MLP comparison additionally requires PyTorch. Install the Python dependencies from the project package before re-running the model matrix.

The paper is organized as a comparative empirical study of twelve risk models: prevalence, dose-only isotonic regression, Ridge regression, softmax spline logistic regression, RBF support-vector regression, weighted KNN, a grouped MLP, a depth-2 decision tree, a multi-output random forest (120 trees, maximum depth 8, minimum leaf size 6), ExtraTrees, histogram gradient boosting, and CatBoost. All formal tables and figures use the same balanced replacement draws; results are compared by metric and risk budget.

Compile locally with:

```bash
mkdir -p build
tectonic --outdir build main.tex
```

The compiled manuscript is kept within the nine-page course limit, including references. All formal results use the balanced replacement evaluation; natural-distribution metrics remain supplemental diagnostics in the experiment package.
