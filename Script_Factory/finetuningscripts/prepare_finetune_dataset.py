#!/usr/bin/env python3
"""
prepare_finetune_dataset.py

Inputs:
 - analysis_dir: directory containing analysis outputs (e.g., analysis/compiled or analyze outputs)
Outputs:
 - dataset.jsonl: filtered, scored JSONL ready for fine-tuning

Heuristics used by default:
 - Score by text length and token-uniqueness proxy (simple heuristics)
 - Remove duplicates by hashing the text
 - Keep top N by score or sample per quant
"""
import argparse, json, hashlib
from pathlib import Path

def score_text(t):
    tokens = t.split()
    uniq = len(set(tokens))
    length = len(tokens)
    # simple heuristic: unique density * log(length)
    import math
    return (uniq / max(1, length)) * math.log(max(2, length))

def dedupe(items):
    seen = set()
    out = []
    for it in items:
        h = hashlib.sha256(it["text"].encode("utf-8")).hexdigest()
        if h in seen: continue
        seen.add(h)
        out.append(it)
    return out

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source_dir", required=True, help="Directory with compiled/analysis text files")
    p.add_argument("--out_file", default="dataset.jsonl")
    p.add_argument("--max_examples", type=int, default=1000)
    args = p.parse_args()

    files = list(Path(args.source_dir).glob("*.txt"))
    items = []
    for f in files:
        txt = f.read_text(encoding="utf-8", errors="ignore")
        # naive split by run separators -- keep whole chunk for now
        items.append({"source_file": str(f), "text": txt, "score": score_text(txt)})
    print("Loaded", len(items), "candidates")

    items = dedupe(items)
    items.sort(key=lambda x: x["score"], reverse=True)
    print("Unique candidates:", len(items))
    selected = items[:args.max_examples]

    # write JSONL: each line {"prompt": "...","completion": "..."} - user may adapt
    with open(args.out_file, "w", encoding="utf-8") as out:
        for it in selected:
            # Here we treat the whole file as a "completion"; you might instead split into (prompt, completion) pairs.
            record = {"source_file": it["source_file"], "text": it["text"], "score": it["score"]}
            out.write(json.dumps(record) + "\n")

    print("Wrote", args.out_file, "with", len(selected), "examples")

if __name__ == "__main__":
    main()
