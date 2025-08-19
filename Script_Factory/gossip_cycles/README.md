# Gossip Cycles Folder

## Purpose
Stores the results of the "prompt ↔ code ↔ prompt" back-and-forth transformations.
Used to study whether repeated conversions stabilize or degrade the code quality (entropy analysis).

## Contents
- Subfolders for each experiment cycle, e.g., `cycle_01`, `cycle_02`, etc.
- Inside each, pairs of:
  - Generated prompt from code
  - Generated code from prompt
- Notes on drift, coherence changes, or bug introduction.

## To-Do
- For each chosen script, run multiple gossip passes and save outputs sequentially.
- Track the number of cycles before noticeable convergence or degradation occurs.
- Compare performance across different LLMs to identify resilience or chaos tendencies.
