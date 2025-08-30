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

class PointlessBlockchainLogger:
    def __init__(self):
        self.chain = []
        self.current_block = None
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block = Block(
            index=0,
            timestamp=datetime.utcnow().isoformat() + 'Z',
            transactions=[],
            prev_hash="0" * 64
        )
        self.chain.append(genesis_block)
        self.current_block = genesis_block
    
    def add_transaction(self, cpu_usage):
        if not self.current_block:
            self.create_genesis_block()
        
        transaction = {
            "time": datetime.utcnow().isoformat() + 'Z',
            "cpu_usage": cpu_usage
        }
        
        self.current_block.transactions.append(transaction)
        
        # Check if we have 10 transactions to finalize the block
        if len(self.current_block.transactions) >= 10:
            self.finalize_block()
    
    def finalize_block(self):
        # Compute the hash of the current block
        self.current_block.hash = self.current_block.compute_hash()
        
        # Print the block in pretty-printed JSON format
        print(json.dumps(self.current_block.__dict__, indent=2))
        
        # Create a new block with the previous block's hash as prev_hash
        new_index = len(self.chain)
        new_timestamp = datetime.utcnow().isoformat() + 'Z'
        new_prev_hash = self.current_block.hash
        
        self.current_block = Block(
            index=new_index,
            timestamp=new_timestamp,
            transactions=[],
            prev_hash=new_prev_hash
        )
        
        # Add the new block to the chain
        self.chain.append(self.current_block)
    
    def run(self):
        try:
            while True:
                cpu_percent = psutil.cpu_percent(interval=1)
                self.add_transaction(cpu_percent)
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    logger = PointlessBlockchainLogger()
    logger.run()
