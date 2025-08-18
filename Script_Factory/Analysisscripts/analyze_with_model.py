#!/usr/bin/env python3
"""
analyze_with_model.py

Run a stronger analysis model (local CLI) over compiled files.

Config:
  - command_template: a shell-style template string with placeholders:
      {model_cli} {model_path} {input_file} {output_file}
  - You can include other CLI args like --threads, --ctx-size, etc.

Example:
  python analyze_with_model.py \
    --compiled_dir analysis/compiled \
    --model_cli "./llama.cpp/main" \
    --model_path models/qwen3-coder-30b.gguf \
    --cmd_template "{model_cli} --model {model_path} --prompt-file {input_file} --out-file {output_file} --ctx-size 8192"

"""
import argparse
import subprocess
import shlex
from pathlib import Path
import json
import time

def run_cmd(template, replacements):
    cmd = template.format(**replacements)
    print("Running:", cmd)
    start = time.time()
    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    end = time.time()
    return proc.returncode, proc.stdout, proc.stderr, end - start

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--compiled_dir", required=True)
    p.add_argument("--out_dir", required=True)
    p.add_argument("--model_cli", required=True, help="Path to inference CLI executable")
    p.add_argument("--model_path", required=True, help="Path to robust model .gguf")
    p.add_argument("--cmd_template", required=True, help="Template with {model_cli},{model_path},{input_file},{output_file}")
    args = p.parse_args()

    compiled_dir = Path(args.compiled_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    summary = {}
    for compiled in compiled_dir.glob("compiled_*.txt"):
        quant = compiled.stem.replace("compiled_","")
        out_file = out_dir / f"analysis_{quant}.txt"
        meta_file = out_dir / f"analysis_{quant}.json"

        replacements = {
            "model_cli": args.model_cli,
            "model_path": args.model_path,
            "input_file": str(compiled),
            "output_file": str(out_file)
        }
        ret, stdout, stderr, elapsed = run_cmd(args.cmd_template, replacements)
        entry = {
            "quant": quant,
            "compiled_input": str(compiled),
            "analysis_output": str(out_file),
            "return_code": ret,
            "stderr": stderr[:2000],
            "elapsed_seconds": elapsed
        }
        with open(meta_file, "w", encoding="utf-8") as mf:
            json.dump(entry, mf, indent=2)

        summary[quant] = entry
    # master summary
    with open(out_dir / "analysis_summary.json", "w", encoding="utf-8") as s:
        json.dump(summary, s, indent=2)

    print("Analysis complete. Summary:", out_dir / "analysis_summary.json")

if __name__ == "__main__":
    main()
