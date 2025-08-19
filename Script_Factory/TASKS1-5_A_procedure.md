this will be use 4A from the readme (prompt-->script only)

1. Order of operations for the Script Factory
If you want the master run script to be really useful from day one, it’s better to do this in this order:

Step 1 — Gather inputs

Refine all prompts first (so no placeholder work later).

Download all .gguf model variants you plan to test.

Since quantization is baked into the .gguf, you need these before runs.

Step 2 — Prototype the master run script

The script can run with a small prompt set & 1–2 model files just to verify logging, folder routing, and metadata creation.

Then you expand it to full prompt/model list.

Step 3 — Scaling up

Kick off overnight runs for one prompt × all model configs → use this to baseline runtimes and confirm metadata accuracy.

Then run all prompts × all models once your workflow is smooth.

Step 4 — Secondary analysis tools

Script to merge runs by type into “mega-files” for LLM review.

Regex cleaner to strip <think> blocks, repeated boilerplate, and other unwanted output into a “cleaned” dataset folder.