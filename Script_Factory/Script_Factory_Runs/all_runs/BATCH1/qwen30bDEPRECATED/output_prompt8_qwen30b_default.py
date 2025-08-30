import psutil
import time
import json
import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, transactions, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.transactions, sort_keys=True)}{self.prev_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

def genesis_block():
    return Block(0, datetime.utcnow().isoformat(), [], "0" * 64)

def main():
    chain = []
    current_block = genesis_block()
    chain.append(current_block)
    
    try:
        while True:
            # Get CPU usage
            cpu_percent = psutil.cpu_percent(interval=1)
            
            # Add transaction to current block
            transaction = {
                "time": datetime.utcnow().isoformat(),
                "cpu_usage": cpu_percent
            }
            current_block.transactions.append(transaction)
            
            # Check if block is full (10 transactions)
            if len(current_block.transactions) == 10:
                # Finalize the block
                current_block.hash = current_block.compute_hash()
                
                # Print the block as JSON
                print(json.dumps(current_block.__dict__, indent=2))
                
                # Create new block with previous hash
                new_block = Block(
                    index=current_block.index + 1,
                    timestamp=datetime.utcnow().isoformat(),
                    transactions=[],
                    prev_hash=current_block.hash
                )
                current_block = new_block
                chain.append(current_block)
                
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
