import chess
import chess.engine
import random

def generate_blunders(board):
    """Generate a list of blunder moves for the current board position."""
    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return []

    blunders = []
    # Add random suboptimal moves
    blunders.extend(random.sample(legal_moves, min(3, len(legal_moves))))

    # Add material sacrifices (if possible)
    for move in legal_moves:
        if board.is_capture(move):
            blunders.append(move)

    return blunders

def self_sabotaging_bot():
    """Play a full game where the same bot plays both sides and intentionally loses."""
    board = chess.Board()
    pgn = chess.pgn.Game()
    pgn.headers["Event"] = "Self-Sabotaging Bot Game"

    move_list = []
    blunder_count = 0
    forced_mate = False

    while not board.is_game_over(claim_draw=True):
        if board.turn:
            color_str = "White"
        else:
            color_str = "Black"

        # Generate possible moves and choose a blunder
        legal_moves = list(board.legal_moves)
        if not legal_moves:
            break

        blunders = generate_blunders(board)

        if blunders:
            chosen_move = random.choice(blunders)
            move_list.append(chosen_move)
            board.push(chosen_move)
            pgn.add_variation(chosen_move)

            # Check if this was a significant blunder
            if board.is_checkmate():
                forced_mate = True
                break
            elif board.is_stalemate() or board.is_insufficient_material() or board.can_claim_draw():
                blunder_count += 1

    # Game over - analyze the result
    result = board.result(claim_draw=True)
    losing_side = "White" if (board.turn and result == "1-0") else "Black"
    outcome = "forced mate" if forced_mate else "blunder"

    print("\nGame Over!")
    print(f"Result: {result}")
    print(f"{losing_side} lost the game by {outcome}")
    print(f"Total moves: {len(move_list)}")
    print(f"Blunders made: {blunder_count}\n")

    # Print PGN
    print("PGN:")
    print(pgn)

if __name__ == "__main__":
    self_sabotaging_bot()

# ===== GENERATED TESTS =====
```python
import pytest
from typing import List

# Original script remains unchanged

def test_generate_blunders():
    """Test the generate_blunders function with different board positions."""
    # Test with a simple board position
    board = chess.Board("8/8/8/3k4/8/8/5Q2/7K w - - 0 1")
    blunders = generate_blunders(board)
    assert isinstance(blunders, list)
    assert len(blunders) <= 3

    # Test with a board position where there are no legal moves
    board = chess.Board("8/8/8/8/8/8/8/8 b - - 0 1")
    blunders = generate_blunders(board)
    assert isinstance(blunders, list)
    assert len(blunders) == 0

def test_self_sabotaging_bot():
    """Test the self_sabotaging_bot function."""
    # Run the bot and capture the output
    with pytest.raises(SystemExit):
        self_sabotaging_bot()

# Add more tests as needed for other public functions and classes
```

This test suite includes two test cases:
1. `test_generate_blunders` to verify that the `generate_blunders` function returns a list of blunder moves and handles different board positions.
2. `test_self_sabotaging_bot` to ensure that the `self_sabotaging_bot` function runs without errors.

You can add more tests as needed for other public functions and classes in the script.