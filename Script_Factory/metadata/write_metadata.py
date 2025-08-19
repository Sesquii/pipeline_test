import os
import json
from datetime import datetime

METADATA_DIR = "metadata"

def write_metadata(
    prompt_id,
    llm_name,
    quantization,
    context_size,
    output_file,
    timestamp_start=None,
    timestamp_end=None,
    extra=None
):
    """
    Write metadata for an LLM run to a JSON file.
    """

    os.makedirs(METADATA_DIR, exist_ok=True)

    # Fallback timestamps if not provided
    if timestamp_start is None:
        timestamp_start = datetime.utcnow().isoformat()
    if timestamp_end is None:
        timestamp_end = datetime.utcnow().isoformat()

    # Calculate elapsed time
    start_dt = datetime.fromisoformat(timestamp_start)
    end_dt = datetime.fromisoformat(timestamp_end)
    elapsed_time = (end_dt - start_dt).total_seconds()

    metadata = {
        "prompt_id": prompt_id,
        "llm_name": llm_name,
        "quantization": quantization,
        "context_size": context_size,
        "output_file": output_file,
        "timestamp_start": timestamp_start,
        "timestamp_end": timestamp_end,
        "elapsed_time_sec": elapsed_time,
    }

    # Add optional extra fields (e.g., params, MoE count, notes)
    if extra:
        metadata.update(extra)

    # Save to JSON (one file per run)
    filename = f"{prompt_id}_{llm_name}_{quantization}.json"
    filepath = os.path.join(METADATA_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"[+] Metadata written → {filepath}")
    return filepath
