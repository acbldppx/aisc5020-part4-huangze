"""Generate LaTeX data tables from Part 4 CSV, then build report separately."""
import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with (root / "outputs/part4/stats/run_summary.csv").open() as f:
    runs = list(csv.DictReader(f))
labels = {"gd": "GD", "heavy_ball": "Heavy ball", "adam": "Adam", "eigenbasis_adam": "Eigenbasis Adam", "diagonal_gd": "Diagonal GD"}
lines = [r"\begin{table}[H]\centering\small", r"\begin{tabular}{llrrr}\toprule",
         r"Regime & Method & Unique runs & Ever attained & Final retained \\ \midrule"]
for regime in ("transfer", "retune", "theory"):
    for algorithm, label in labels.items():
        selected = [r for r in runs if r["regime"] == regime and r["algorithm"] == algorithm and r["checkpoint"] == "50000"]
        if selected:
            counts = [sum(int(r[key]) for r in selected) for key in ("n_runs", "ever_attained", "final_retained")]
            lines.append(f"{regime} & {label} & {counts[0]} & {counts[1]} & {counts[2]} " + r"\\")
lines.extend([r"\bottomrule\end{tabular}", r"\caption{Unique evaluation runs; references counted once. Theory is separate.}", r"\end{table}"])
(root / "docs/part4_generated_tables.tex").write_text("\n".join(lines) + "\n")
