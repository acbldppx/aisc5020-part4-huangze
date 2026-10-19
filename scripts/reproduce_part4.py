"""Reproduce only Module 4, not the expensive Part 3 tuning/evaluation.

Run from project root: python scripts/reproduce_part4.py --report
Requires numpy, matplotlib; --report additionally requires pdflatex on PATH.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--report", action="store_true")
args = parser.parse_args()
config = json.loads((root / "configs/part4.json").read_text())
env = dict(os.environ, PYTHONPATH=str(root / "src"), OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1")

def run(*command, cwd=root, log=None):
    if log:
        with log.open("w") as handle:
            subprocess.run(command, cwd=cwd, env=env, stdout=handle, stderr=subprocess.STDOUT, check=True)
    else:
        subprocess.run(command, cwd=cwd, env=env, check=True)

run(sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q")
run(sys.executable, "-m", "coordinate_geometry.part4_experiments", "--output", "outputs/part4")
run(sys.executable, "-m", "coordinate_geometry.part4_statistics", "--input", config["input"],
    "--output", config["statistics_output"], "--bootstrap", str(config["bootstrap_repetitions"]), "--seed", str(config["bootstrap_seed"]))
run(sys.executable, "-m", "coordinate_geometry.part4_figures")
run(sys.executable, "scripts/part4_tables.py")
if args.report:
    if not shutil.which("pdflatex"):
        raise SystemExit("Statistics are complete. Install a LaTeX distribution to rebuild the included PDF.")
    for _ in range(2):
        run("pdflatex", "-interaction=nonstopmode", "-halt-on-error", "part4_report.tex", cwd=root / "docs", log=root / "outputs/part4/report_build.log")
    shutil.copy2(root / "docs/part4_report.pdf", root / "outputs/part4/part4_report.pdf")
print("Part 4 recomputed. This does NOT assert a fully passing historical optimizer replay.")
