#!/usr/bin/env python3
"""
compile_by_quant.py

Collates raw outputs grouped by quantization and writes:
  - per-quant concatenated file (for human/LLM review)
  - an index JSON listing source files & metadata

Usage:
  python compile_by_quant.py --all_runs_dir "Script_Factory_Runs/all_runs" --out_dir "analysis/compiled"
"""
import argparse
import json
import os
from pathlib import Path
from collections import defaultdict

def load_metadata(mjson_path):
    try:
        with open(mjson_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--all_runs_dir", required=True)
    p.add_argument("--out_dir", required=True)
    args = p.parse_args()

    all_runs = Path(args.all_runs_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Expect structure: all_runs/<runid>.txt and all_runs/<runid>.json
    quant_buckets = defaultdict(list)

    for meta_file in all_runs.glob("*.json"):
        meta = load_metadata(meta_file)
        if not meta: 
            print(f"Skipping invalid metadata: {meta_file}")
            continue
        quant = meta.get("quantization", "UNKNOWN")
        text_file = all_runs / meta.get("output_file", meta_file.with_suffix(".txt").name)
        if not text_file.exists():
            # try same name as json but .txt
            alt = meta_file.with_suffix(".txt")
            if alt.exists():
                text_file = alt
            else:
                print(f"Output text missing for {meta_file}: looked for {text_file}")
                continue
        quant_buckets[quant].append({"meta": meta, "text_path": str(text_file)})

    summary_index = {}
    for quant, items in quant_buckets.items():
        out_txt = out_dir / f"compiled_{quant}.txt"
        with open(out_txt, "w", encoding="utf-8") as out:
            for it in items:
                meta = it["meta"]
                text_path = it["text_path"]
                out.write(f"--- RUN: {meta.get('run_id','unknown')} ---\n")
                out.write(f"METADATA: {json.dumps(meta)}\n\n")
                with open(text_path, "r", encoding="utf-8", errors="ignore") as tf:
                    out.write(tf.read())
                    out.write("\n\n\n")
        summary_index[quant] = {
            "compiled_file": str(out_txt),
            "count": len(items),
            "examples": [i["meta"]["run_id"] for i in items[:5]]
        }

    # Write index file
    with open(out_dir / "summary_index.json", "w", encoding="utf-8") as idx:
        json.dump(summary_index, idx, indent=2)

    print("Compiled quant buckets:", list(summary_index.keys()))

if __name__ == "__main__":
    main()
