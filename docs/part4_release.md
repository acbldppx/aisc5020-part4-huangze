# Suggested release: part4-v1

Module 4: diagonal preconditioning and paired statistical analysis (HUANG Ze).

Contains P5 derivation, standalone numerical validation, a read-only analysis of
10,200 saved evaluation runs / 6,600 pairs, joint/cluster bootstrap (2,000 draws),
CSV tables, plots, module report PDF/LaTeX, tests and reproduction instructions.

Data provenance: historical Part 3 execution 575ebf4; integration base bb365b9.
All original result bytes are preserved in the complete delivery archive.

Important limitation: structural checks pass; current sampled numerical replay
does not fully pass. The report analyzes historical observations and does not
claim fully reproduced long-horizon optimizer trajectories or controlled timing.

## Publishing from your own account

No GitHub remote has been modified by this delivery. Use your own fork or an
authorized team repository. In GitHub Desktop, fork/clone the team repository,
create feature/part4-statistics, and copy only part4_merge/ files. Review the
diff, commit and push that branch, then open a Pull Request to the integrator.
Do not overwrite unrelated files or push straight to main.

After teammate review/merge, create a release with tag part4-v1 on the reviewed
commit and attach the complete delivery ZIP. Verify the asset is downloadable.
Until those manual steps succeed, there is no published Part 4 GitHub URL.

Large raw results belong in release assets, not ordinary Git blobs. Keep the
team repository private if course rules prohibit publishing assignment material.
