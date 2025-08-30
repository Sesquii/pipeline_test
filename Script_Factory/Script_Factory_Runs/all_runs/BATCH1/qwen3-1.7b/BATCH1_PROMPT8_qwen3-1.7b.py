```python
import psutil
import datetime
import json
import hashlib

def compute_block_hash(block):
    """Compute SHA-256 hash of a block's data."""
    data = f"{block['index']} {block['timestamp']} {''.join(json.dumps(block['transactions']))} {block['prev_hash']}"
    return hashlib.sha256(data.encode()).hexdigest()

# Genesis block with initial configuration
genesis_block = {
    "index": 0,
    "timestamp": datetime.datetime.utcnow().isoformat(),
    "transactions": [],
    "prev_hash": '0' * 64,
    "hash": compute_block_hash(genesis_block)
}

blockchain = [genesis_block]
current_block = genesis_block

while True:
    # Monitor CPU usage every second
    cpu_usage = psutil.cpu_percent()
    current_time = datetime.datetime.utcnow().isoformat()

    # Add the current CPU reading as a transaction to the current block
    current_block['transactions'].append({
        "time": current_time,
        "cpu_usage": cpu_usage
    })

    # Check if we've reached 10 transactions and finalize a new block
    if len(current_block['transactions']) == 10:
        new_block = {
            "index": len(blockchain),
            "timestamp": current_time,
            "transactions": current_block['transactions'],
            "prev_hash": compute_block_hash(blockchain[-1]),
            "hash": compute_block_hash(new_block)
        }

        blockchain.append(new_block)

        # Print the newly created block in pretty JSON format
        print(json.dumps(new_block, indent=4))

        # Reset to a new block for subsequent processing
        current_block = new_block