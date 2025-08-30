import json
import hashlib
import time
from datetime import datetime
import psutil

class Block:
    def __init__(self, index, timestamp, transactions=None, prev_hash="0" * 64):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions if transactions else []
        self.prev_hash = prev_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.transactions)}{self.prev_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "prev_hash": self.prev_hash,
            "hash": self.hash
        }

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.utcnow().isoformat(), prev_hash="0" * 64)

    def add_transaction(self, transaction):
        current_block = self.chain[-1]
        if len(current_block.transactions) < 10:
            current_block.transactions.append(transaction)
        else:
            self.finalize_block()
            new_block = Block(len(self.chain), datetime.utcnow().isoformat(), prev_hash=current_block.hash)
            new_block.transactions.append(transaction)
            self.chain.append(new_block)

    def finalize_block(self):
        current_block = self.chain[-1]
        print(json.dumps(current_block.to_dict(), indent=2))
        # Note: We don't need to update the hash here since it's computed in the constructor

def main():
    blockchain = Blockchain()
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            transaction = {
                "time": datetime.utcnow().isoformat(),
                "cpu_usage": cpu_usage
            }
            blockchain.add_transaction(transaction)
    except KeyboardInterrupt:
        # Finalize any remaining block when program is stopped
        if len(blockchain.chain[-1].transactions) > 0:
            print(json.dumps(blockchain.chain[-1].to_dict(), indent=2))

if __name__ == "__main__":
    main()