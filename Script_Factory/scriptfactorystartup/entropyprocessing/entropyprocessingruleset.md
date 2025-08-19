# Entropy Processing Simulation & Ruleset — PIF

## Overview
This document defines the conceptual framework for measuring and simulating entropy in LLM-generated code and natural language prompts.

---

## Core Entropy Metrics

1. **Capacity**
   - Definition: Potential of a prompt to produce high-chaos or error-prone code.
   - Scale: 1–10 (low chaos → high chaos)

2. **Entropic Allure**
   - Definition: How “human-chaotic” the idea sounds when expressed in natural language.
   - Scale: 1–10 (dry → wildly vivid)

3. **Entropy Orientation**
   - Definition: Whether converting the prompt to code increases (+) or decreases (–) entropy.
   - Scale: `+` for chaos amplification, `–` for chaos reduction.

4. **Baseline Entropy**
   - Formula: `(Capacity * 0.5) + (Allure * 0.3) + (OrientationFactor * 0.2)`
   - `OrientationFactor` = Capacity if `+`, else `10 - Capacity`.

---

## Simulation Modes

1. **4A — Prompt → Code**
2. **4B — Prompt + Reference Code → Optimized Code**
3. **4C — Code Only → Optimized Code**
4. **4D — Code Only → Hallucinated Prompt**
5. **4E — Gossip Simulation**
   - Cycle between Prompt → Code → Prompt repeatedly.
   - Observe stabilization vs. divergence of entropy.

---

## Notes
- Do not filter out “bad” outputs — high entropy is desirable for study.
- Log model name, quantization, prompt, and output for all runs.
- Repeat across multiple LLM sizes to compare entropy behavior.
- Use Baseline Entropy to prioritize which prompts to run first.
