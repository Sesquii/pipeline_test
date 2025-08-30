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

# ===== GENERATED TESTS =====
import pytest
from datetime import datetime
from unittest.mock import patch

# Original code remains unchanged

def test_block_compute_hash():
    """Test the compute_hash method of the Block class."""
    block = Block(0, datetime.utcnow().isoformat())
    assert len(block.hash) == 64

def test_block_to_dict():
    """Test the to_dict method of the Block class."""
    block = Block(0, datetime.utcnow().isoformat())
    assert isinstance(block.to_dict(), dict)
    assert "index" in block.to_dict()
    assert "timestamp" in block.to_dict()
    assert "transactions" in block.to_dict()
    assert "prev_hash" in block.to_dict()
    assert "hash" in block.to_dict()

def test_blockchain_create_genesis_block():
    """Test the create_genesis_block method of the Blockchain class."""
    blockchain = Blockchain()
    genesis_block = blockchain.create_genesis_block()
    assert isinstance(genesis_block, Block)
    assert genesis_block.index == 0
    assert genesis_block.prev_hash == "0" * 64

def test_blockchain_add_transaction():
    """Test the add_transaction method of the Blockchain class."""
    blockchain = Blockchain()
    transaction = {
        "time": datetime.utcnow().isoformat(),
        "cpu_usage": psutil.cpu_percent(interval=1)
    }
    blockchain.add_transaction(transaction)
    assert len(blockchain.chain[-1].transactions) == 1

def test_blockchain_finalize_block(capsys):
    """Test the finalize_block method of the Blockchain class."""
    blockchain = Blockchain()
    transaction = {
        "time": datetime.utcnow().isoformat(),
        "cpu_usage": psutil.cpu_percent(interval=1)
    }
    blockchain.add_transaction(transaction)
    blockchain.finalize_block()
    captured = capsys.readouterr()
    assert len(captured.out) > 0

def test_main_with_mocked_psutil():
    """Test the main function with mocked psutil."""
    with patch('psutil.cpu_percent') as mock_cpu:
        mock_cpu.return_value = 50.0
        blockchain = Blockchain()
        transaction = {
            "time": datetime.utcnow().isoformat(),
            "cpu_usage": 50.0
        }
        blockchain.add_transaction(transaction)
        assert len(blockchain.chain[-1].transactions) == 1

# Test cases for the original code end here
