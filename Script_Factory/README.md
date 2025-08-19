# 🏭 Script Factory — README

## Overview
The **Script Factory** is a controlled experiment pipeline designed to produce, process, and compare *high-entropy* code outputs from multiple Large Language Models (LLMs).  
Rather than aiming for "perfect" scripts, this system **deliberately encourages flawed, inefficient, or unusual outputs** so we can study how different models behave, hallucinate, and optimize under varying conditions.

The factory is a structured environment to:
- Mass-produce pseudo-identical scripts from diverse models.
- Run entropy-based analysis (Task 4).
- Observe how calibration levels (INT2, FP16, FP32, etc.) and parameter sizes affect code generation.
- Improve intuition for LLM behavior by *trialing errors* — then learning from them.

---

## Project Intent
The Script Factory is meant to:
1. **Characterize** the "chaos signature" of different LLMs.
2. **Compare** open source vs. closed source models in controlled conditions.
3. **Quantify** how prompt style and context affect entropy in generated code.
4. **Simulate** prompt/code drift (gossip effect) across multiple conversion cycles.
5. **Enhance** personal understanding of LLM mechanics through hands-on testing.

This is not a code quality competition — **we embrace imperfection** here.

---

## Core Benefits
- **Multi-model insight**: See how 10+ LLMs interpret the same script prompt.
- **Entropy profiling**: Measure and rank prompts by their chaos potential.
- **Optimization trials**: Compare naive outputs vs. optimized code from small and large LLMs.
- **Calibration effects**: Quantify how quantization/precision impacts generation style.
- **Long-term trend data**: Use gossip simulation to track entropy stability vs. escalation.

---

## Procedure Summary

**Task 1 — Script Prompt Generation**
- 25 *hallucinated prompt ideas* designed for high-entropy code.
- Each prompt forms a "script implementation unit."

**Task 2 — Multi-LLM Generation**
- For each prompt, run **10 LLMs** to produce pseudo-identical scripts.
- Output = 250 raw scripts.

**Task 3 — Optimization & Variation**
- Run the **4A–4D pipeline** on each script:
  - 4A: Prompt → Code
  - 4B: Prompt + Reference Code → Optimized Code
  - 4C: Code Only → Optimized Code
  - 4D: Code Only → Hallucinated Prompt
  - *(Optional 4E)*: Gossip Simulation loop

**Task 4 — Entropy Processing**
- Use `entropyprocessing.md` rules to rank scripts by:
  - Capacity
  - Entropic Allure
  - Orientation
  - Baseline Entropy

**Task 5 — Cross-Comparison**
- Compare outputs across:
  - Model types (OSS vs closed)
  - Calibration levels (INT2, FP16, FP32)
  - Parameter sizes (20B vs 120B, etc.)

---

## Estimated Prompt & Script Counts

| Category | Per Unit (1 prompt) | Full Project (25 prompts) |
|----------|--------------------|---------------------------|
| Open Source Model Prompts | 10 | 250 |
| Closed Source Model Prompts | 10 | 250 |
| **Total Prompts** | 20 | 500 |
| Generated Scripts (Raw) | 20 | 500 |
| Generated Scripts (With 4A–4D) | 80 | 2,000 |

---

## Resource Notes
- LLM Count: ~10 OSS, ~10 closed-source/hosted.
- Expected Script Length: 30–200 lines (varies by model).
- Storage Requirement: ~50–200 KB per script, plus logs.
- Agent Usage: Heavy — detailed load prediction will be in `agenticloadofscriptfactory.md`.

---

## Output Structure
