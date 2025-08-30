import time
import json
from datetime import datetime
import hashlib
import psutil

# Function to calculate the SHA-256 hash of a string
def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Class representing a block in the blockchain
class Block:
    def __init__(self, index, timestamp, transactions, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.hash = calculate_hash(self.index + self.timestamp + json.dumps(self.transactions) + self.prev_hash)

# Initialize the blockchain with the genesis block
blockchain = [Block(0, datetime.utcnow().isoformat(), [], "0"*64)]
current_block_index = 1
current_transactions = []

# Function to mine a new block and add it to the blockchain
def mine_block():
    global current_block_index, current_transactions
    if not current_transactions:
        return
    
    # Finalize the current block
    new_block = Block(current_block_index, datetime.utcnow().isoformat(), current_transactions, blockchain[-1].hash)
    
    # Print the new block as a pretty-printed JSON object
    print(json.dumps(new_block.__dict__, indent=4))
    
    # Start a new empty block with the appropriate prev_hash
    current_block_index += 1
    current_transactions = []

# Main loop to continuously monitor CPU usage and create blocks
try:
    while True:
        # Get the current CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Add a new transaction with the CPU usage
        current_transactions.append({
            "time": datetime.utcnow().isoformat(),
            "cpu_usage": cpu_usage,
            "prev_hash": blockchain[-1].hash if blockchain else ""
        })
        
        # If 10 transactions are added, mine a new block
        if len(current_transactions) >= 10:
            mine_block()
except KeyboardInterrupt:
    print("Blockchain logger stopped by user.")
```

This Python program implements the "Pointless Blockchain Logger" as described. It uses the `psutil` library to monitor CPU usage and constructs an in-memory blockchain where each block contains transactions of CPU usages. When 10 transactions are collected, it finalizes the block, computes its hash, appends it to the chain, and prints the block as a pretty-printed JSON object immediately after creation. The program runs indefinitely until manually stopped with Ctrl+C.