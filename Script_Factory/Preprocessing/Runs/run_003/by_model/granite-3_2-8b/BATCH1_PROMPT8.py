import psutil
import time
import json
import hashlib
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return {
            'index': 0,
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': [],
            'prev_hash': '0' * 64,
            'hash': self.compute_hash()
        }

    def create_new_block(self, prev_block):
        new_block = {
            'index': prev_block['index'] + 1,
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': [],
            'prev_hash': prev_block['hash'],
            'hash': self.compute_hash()
        }
        return new_block

    def compute_hash(self, block):
        block_string = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_transaction(self, block, cpu_usage):
        block['transactions'].append({
            'time': datetime.utcnow().isoformat(),
            'cpu_usage': cpu_usage
        })

        if len(block['transactions']) >= 10:
            new_block = self.create_new_block(block)
            self.chain.append(new_block)
            print(json.dumps(new_block, indent=4))

def main():
    blockchain = Blockchain()

    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        current_block = blockchain.chain[-1]
        blockchain.add_transaction(current_block, cpu_usage)

        time.sleep(1)

if __name__ == "__main__":
    main()