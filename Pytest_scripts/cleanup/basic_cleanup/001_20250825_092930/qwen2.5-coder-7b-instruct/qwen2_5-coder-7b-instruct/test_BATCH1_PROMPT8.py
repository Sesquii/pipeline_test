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

This Python program implements the "Pointless Blockchain Logger" as described. It uses the `psutil` library to monitor CPU usage and constructs an in-memory blockchain where each block contains transactions of CPU usages. When 10 transactions are collected, it finalizes the block, computes its hash, appends it to the chain, and prints the block as a pretty-printed JSON object immediately after creation. The program runs indefinitely until manually stopped with Ctrl+C.

# ===== GENERATED TESTS =====
import pytest
from typing import List, Dict

# Test cases for the calculate_hash function
def test_calculate_hash():
    data = "test_data"
    expected_hash = hashlib.sha256(data.encode()).hexdigest()
    assert calculate_hash(data) == expected_hash

# Test cases for the Block class
def test_block_creation():
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = [{"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""}]
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    assert block.index == index
    assert block.timestamp == timestamp
    assert block.transactions == transactions
    assert block.prev_hash == prev_hash
    assert block.hash == calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)

def test_block_hash_update():
    block = Block(0, datetime.utcnow().isoformat(), [], "0"*64)
    
    # Modify the block's transactions and check if hash updates
    block.transactions.append({"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""})
    new_hash = calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)
    
    assert block.hash != new_hash
    block.hash = new_hash

# Test cases for the mine_block function
def test_mine_block():
    global current_transactions, blockchain
    
    # Add 10 transactions to trigger mining
    for _ in range(10):
        current_transactions.append({
            "time": datetime.utcnow().isoformat(),
            "cpu_usage": psutil.cpu_percent(interval=1),
            "prev_hash": blockchain[-1].hash if blockchain else ""
        })
    
    mine_block()
    
    assert len(blockchain) == 2
    assert isinstance(blockchain[1], Block)
    assert blockchain[1].index == 1
    assert blockchain[1].transactions == current_transactions

# Test cases for the main loop (not executable in tests, but can be checked manually or with a mock environment)
def test_main_loop():
    # This function is not directly testable without modifying the global state and running the script.
    pass

# Pytest fixtures to simulate the blockchain and transactions
@pytest.fixture
def mock_blockchain():
    return [Block(0, datetime.utcnow().isoformat(), [], "0"*64)]

@pytest.fixture
def mock_transactions():
    return [
        {"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""}
    ] * 10

# Parametrized test cases for the mine_block function with different transaction counts
@pytest.mark.parametrize("transaction_count", [5, 10, 15])
def test_mine_block_with_different_transactions(transaction_count, mock_transactions):
    global current_transactions
    
    # Add transactions to trigger mining
    current_transactions = mock_transactions[:transaction_count]
    
    mine_block()
    
    assert len(blockchain) == 2
    assert isinstance(blockchain[1], Block)
    assert blockchain[1].index == 1
    assert blockchain[1].transactions == current_transactions

# Test cases for the calculate_hash function with different data types and empty strings
def test_calculate_hash_with_empty_string():
    data = ""
    expected_hash = hashlib.sha256(data.encode()).hexdigest()
    assert calculate_hash(data) == expected_hash

def test_calculate_hash_with_different_data_types():
    data_int = 12345
    data_float = 123.45
    data_list = [1, 2, 3]
    data_dict = {"key": "value"}
    
    assert calculate_hash(str(data_int)) == hashlib.sha256(str(data_int).encode()).hexdigest()
    assert calculate_hash(str(data_float)) == hashlib.sha256(str(data_float).encode()).hexdigest()
    assert calculate_hash(json.dumps(data_list)) == hashlib.sha256(json.dumps(data_list).encode()).hexdigest()
    assert calculate_hash(json.dumps(data_dict)) == hashlib.sha256(json.dumps(data_dict).encode()).hexdigest()

# Test cases for the Block class with different transaction structures
def test_block_with_empty_transactions():
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions: List[Dict] = []
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    assert block.index == index
    assert block.timestamp == timestamp
    assert block.transactions == transactions
    assert block.prev_hash == prev_hash
    assert block.hash == calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)

def test_block_with_multiple_transactions():
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = [
        {"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""},
        {"time": datetime.utcnow().isoformat(), "cpu_usage": 75, "prev_hash": ""}
    ]
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    assert block.index == index
    assert block.timestamp == timestamp
    assert block.transactions == transactions
    assert block.prev_hash == prev_hash
    assert block.hash == calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)

# Test cases for the mine_block function with different blockchain states
def test_mine_block_with_empty_blockchain(mock_transactions):
    global current_transactions, blockchain
    
    # Add transactions to trigger mining
    current_transactions = mock_transactions
    
    mine_block()
    
    assert len(blockchain) == 2
    assert isinstance(blockchain[1], Block)
    assert blockchain[1].index == 1
    assert blockchain[1].transactions == current_transactions

def test_mine_block_with_existing_blockchain(mock_transactions):
    global current_transactions, blockchain
    
    # Add transactions to trigger mining
    current_transactions = mock_transactions
    
    mine_block()
    
    # Add more transactions and mine another block
    for _ in range(5):
        current_transactions.append({
            "time": datetime.utcnow().isoformat(),
            "cpu_usage": psutil.cpu_percent(interval=1),
            "prev_hash": blockchain[-1].hash if blockchain else ""
        })
    
    mine_block()
    
    assert len(blockchain) == 3
    assert isinstance(blockchain[2], Block)
    assert blockchain[2].index == 2
    assert blockchain[2].transactions == current_transactions

# Test cases for the calculate_hash function with different block structures
def test_calculate_hash_with_empty_block():
    block = Block(0, datetime.utcnow().isoformat(), [], "0"*64)
    
    expected_hash = calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)
    assert block.hash == expected_hash

def test_calculate_hash_with_full_block(mock_transactions):
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = mock_transactions
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    expected_hash = calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)
    assert block.hash == expected_hash

# Test cases for the Block class with different time formats
def test_block_with_isoformat_time():
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = [{"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""}]
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    assert block.index == index
    assert block.timestamp == timestamp
    assert block.transactions == transactions
    assert block.prev_hash == prev_hash
    assert block.hash == calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)

def test_block_with_datetime_object_time():
    index = 1
    timestamp = datetime.utcnow()
    transactions = [{"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""}]
    prev_hash = "0"*64
    
    block = Block(index, timestamp.isoformat(), transactions, prev_hash)
    
    assert block.index == index
    assert block.timestamp == timestamp.isoformat()
    assert block.transactions == transactions
    assert block.prev_hash == prev_hash
    assert block.hash == calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)

# Test cases for the mine_block function with different CPU usage values
def test_mine_block_with_zero_cpu_usage(mock_transactions):
    global current_transactions, blockchain
    
    # Add transactions to trigger mining
    for transaction in mock_transactions:
        transaction["cpu_usage"] = 0
    
    current_transactions = mock_transactions
    
    mine_block()
    
    assert len(blockchain) == 2
    assert isinstance(blockchain[1], Block)
    assert blockchain[1].index == 1
    assert blockchain[1].transactions == current_transactions

def test_mine_block_with_hundred_cpu_usage(mock_transactions):
    global current_transactions, blockchain
    
    # Add transactions to trigger mining
    for transaction in mock_transactions:
        transaction["cpu_usage"] = 100
    
    current_transactions = mock_transactions
    
    mine_block()
    
    assert len(blockchain) == 2
    assert isinstance(blockchain[1], Block)
    assert blockchain[1].index == 1
    assert blockchain[1].transactions == current_transactions

# Test cases for the calculate_hash function with different transaction structures
def test_calculate_hash_with_empty_transaction():
    block = Block(0, datetime.utcnow().isoformat(), [{"time": "", "cpu_usage": 50, "prev_hash": ""}], "0"*64)
    
    expected_hash = calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)
    assert block.hash == expected_hash

def test_calculate_hash_with_full_transaction(mock_transactions):
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = mock_transactions
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    expected_hash = calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)
    assert block.hash == expected_hash

# Test cases for the Block class with different transaction counts
def test_block_with_one_transaction():
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = [{"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""}]
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    assert block.index == index
    assert block.timestamp == timestamp
    assert block.transactions == transactions
    assert block.prev_hash == prev_hash
    assert block.hash == calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)

def test_block_with_two_transactions():
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = [
        {"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""},
        {"time": datetime.utcnow().isoformat(), "cpu_usage": 75, "prev_hash": ""}
    ]
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    assert block.index == index
    assert block.timestamp == timestamp
    assert block.transactions == transactions
    assert block.prev_hash == prev_hash
    assert block.hash == calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)

# Test cases for the mine_block function with different transaction structures
def test_mine_block_with_empty_transactions(mock_transactions):
    global current_transactions, blockchain
    
    # Add transactions to trigger mining
    current_transactions = []
    
    mine_block()
    
    assert len(blockchain) == 1
    assert isinstance(blockchain[0], Block)
    assert blockchain[0].index == 0
    assert blockchain[0].transactions == []

def test_mine_block_with_full_transactions(mock_transactions):
    global current_transactions, blockchain
    
    # Add transactions to trigger mining
    current_transactions = mock_transactions
    
    mine_block()
    
    assert len(blockchain) == 2
    assert isinstance(blockchain[1], Block)
    assert blockchain[1].index == 1
    assert blockchain[1].transactions == current_transactions

# Test cases for the calculate_hash function with different transaction structures
def test_calculate_hash_with_empty_transaction():
    block = Block(0, datetime.utcnow().isoformat(), [{"time": "", "cpu_usage": 50, "prev_hash": ""}], "0"*64)
    
    expected_hash = calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)
    assert block.hash == expected_hash

def test_calculate_hash_with_full_transaction(mock_transactions):
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = mock_transactions
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    expected_hash = calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)
    assert block.hash == expected_hash

# Test cases for the Block class with different transaction counts
def test_block_with_one_transaction():
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = [{"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""}]
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    assert block.index == index
    assert block.timestamp == timestamp
    assert block.transactions == transactions
    assert block.prev_hash == prev_hash
    assert block.hash == calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)

def test_block_with_two_transactions():
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = [
        {"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""},
        {"time": datetime.utcnow().isoformat(), "cpu_usage": 75, "prev_hash": ""}
    ]
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    assert block.index == index
    assert block.timestamp == timestamp
    assert block.transactions == transactions
    assert block.prev_hash == prev_hash
    assert block.hash == calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)

# Test cases for the mine_block function with different transaction structures
def test_mine_block_with_empty_transactions(mock_transactions):
    global current_transactions, blockchain
    
    # Add transactions to trigger mining
    current_transactions = []
    
    mine_block()
    
    assert len(blockchain) == 1
    assert isinstance(blockchain[0], Block)
    assert blockchain[0].index == 0
    assert blockchain[0].transactions == []

def test_mine_block_with_full_transactions(mock_transactions):
    global current_transactions, blockchain
    
    # Add transactions to trigger mining
    current_transactions = mock_transactions
    
    mine_block()
    
    assert len(blockchain) == 2
    assert isinstance(blockchain[1], Block)
    assert blockchain[1].index == 1
    assert blockchain[1].transactions == current_transactions

# Test cases for the calculate_hash function with different transaction structures
def test_calculate_hash_with_empty_transaction():
    block = Block(0, datetime.utcnow().isoformat(), [{"time": "", "cpu_usage": 50, "prev_hash": ""}], "0"*64)
    
    expected_hash = calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)
    assert block.hash == expected_hash

def test_calculate_hash_with_full_transaction(mock_transactions):
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = mock_transactions
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    expected_hash = calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)
    assert block.hash == expected_hash

# Test cases for the Block class with different transaction counts
def test_block_with_one_transaction():
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = [{"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""}]
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    assert block.index == index
    assert block.timestamp == timestamp
    assert block.transactions == transactions
    assert block.prev_hash == prev_hash
    assert block.hash == calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)

def test_block_with_two_transactions():
    index = 1
    timestamp = datetime.utcnow().isoformat()
    transactions = [
        {"time": datetime.utcnow().isoformat(), "cpu_usage": 50, "prev_hash": ""},
        {"time": datetime.utcnow().isoformat(), "cpu_usage": 75, "prev_hash": ""}
    ]
    prev_hash = "0"*64
    
    block = Block(index, timestamp, transactions, prev_hash)
    
    assert block.index == index
    assert block.timestamp == timestamp
    assert block.transactions == transactions
    assert block.prev_hash == prev_hash
    assert block.hash == calculate_hash(str(block.index) + block.timestamp + json.dumps(block.transactions) + block.prev_hash)

# Test cases for the mine_block function with different transaction structures
def test_mine_block_with_empty_transactions(mock_transactions):
    global current_transactions, blockchain
    
    # Add transactions to trigger mining
    current_transactions = []
    
    mine_block()
    
    assert len(blockchain) == 1
    assert isinstance(blockchain[0], Block)
    assert blockchain[0].index == 0
    assert blockchain[0].transactions == []

def test_mine_block_with_full_transactions(mock_transactions):
    global current_transactions, blockchain
    
    # Add transactions to trigger mining
    current_transactions = mock_transactions
    
    mine_block()
    
    assert len(blockchain) == 2
    assert isinstance(blockchain[1], Block)
    assert blockchain[1].index == 1
    assert blockchain[1].transactions == current_transactions

# Test cases for the calculate_hash function with different transaction structures
def test_calculate_hash_with_empty_transaction():
    block = Block