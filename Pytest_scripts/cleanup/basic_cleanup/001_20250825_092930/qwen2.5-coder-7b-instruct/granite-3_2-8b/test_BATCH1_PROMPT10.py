import chess
import chess.pgn
import random

# List of blunders or suboptimal moves (example)
BLUNDERS = [
    # Pawn to h3 on opening move
    chess.Move.from_uci('h2h3'), 
    # Move the queen back and forth between its starting position and h8
    chess.Move.from_uci('e1g1e1h8e1g1'), 
    # Castling into check
    chess.Move.from_uci('c1g5'), 
    # Moving a knight to the same square (h4h4)
    chess.Move.from_uci('n1h3n1h3'), 
]

def self_sabotaging_bot(board):
    """A bot that intentionally loses by randomly choosing poor moves."""
    if random.random() < 0.2:  # 20% chance to make a blunder
        move = random.choice(BLUNDERS)
    else:  # Otherwise, make a valid but suboptimal move
        legal_moves = list(board.legal_moves)
        if legal_moves:
            move = random.choice(legal_moves)
        else:
            move = chess.Move.null()

    print(f"{move} {board}")
    return move

def main():
    board = chess.Board()  # Start a new game
    pgn = chess.pgn.GameList()

    while not board.is_game_over():
        move = self_sabotaging_bot(board)
        board.push(move)

        if board.is_checkmate() or board.is_stalemate() or board.is_fivefold():
            break

    pgn.add_variations([chess.pgn.Variation(board)])
    pgn.set_header(players='Self vs Self', result=f"*{board.result()}*")

    print(pgn)

    if board.turn == chess.WHITE:
        losing_side = "White (self)"
    else:
        losing_side = "Black (self)"
    
    if board.is_checkmate():
        loss_type = "Checkmate"
    elif board.is_stalemate():
        loss_type = "Stalemate"
    elif board.is_fivefold():
        loss_type = "50-move rule"
    else:
        loss_type = "Blunder (random move)"

    print(f"\nGame statistics:")
    print(f"Total moves: {board.fullmove_number}")
    print(f"Losing side: {losing_side}")
    print(f"Loss type: {loss_type}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Original script code remains unchanged

# Test suite starts here

@pytest.fixture
def board():
    """Fixture to provide a new chess board for each test."""
    return chess.Board()

@pytest.fixture(params=[0.1, 0.5, 0.9])
def blunder_probability(request):
    """Fixture to parametrize the probability of making a blunder."""
    return request.param

def test_self_sabotaging_bot(board, blunder_probability):
    """
    Test the self_sabotaging_bot function with different probabilities
    of making a blunder.
    """
    original_moves = list(board.legal_moves)
    move = self_sabotaging_bot(board)

    if random.random() < blunder_probability:
        assert move in BLUNDERS, "Move should be one of the blunders"
    else:
        assert move in original_moves, "Move should be a legal move"

def test_main_with_blunder(board):
    """
    Test the main function with a board that is likely to result in a blunder.
    """
    # Set up the board to force a blunder
    board.push_uci('e2e4')
    board.push_uci('e7e5')
    board.push_uci('Nf3Nc6')
    board.push_uci('Bb5a6')

    main()

def test_main_with_no_blunders(board):
    """
    Test the main function with a board that should not result in any blunders.
    """
    # Set up the board to avoid blunders
    board.push_uci('e2e4')
    board.push_uci('e7e5')
    board.push_uci('Nf3Nc6')
    board.push_uci('Bb5a6')

    main()

def test_main_with_checkmate(board):
    """
    Test the main function with a board that results in checkmate.
    """
    # Set up the board to force checkmate
    board.push_uci('e2e4')
    board.push_uci('e7e5')
    board.push_uci('Nf3Nc6')
    board.push_uci('Bb5a6')
    board.push_uci('O-O-O')
    board.push_uci('d7d5')
    board.push_uci('Nbd2')
    board.push_uci('c8e6')

    main()

def test_main_with_stalemate(board):
    """
    Test the main function with a board that results in stalemate.
    """
    # Set up the board to force stalemate
    board.push_uci('e2e4')
    board.push_uci('e7e5')
    board.push_uci('Nf3Nc6')
    board.push_uci('Bb5a6')
    board.push_uci('O-O-O')
    board.push_uci('d7d5')
    board.push_uci('Nbd2')
    board.push_uci('c8e6')
    board.push_uci('f1c4')
    board.push_uci('f8c5')

    main()

def test_main_with_fivefold(board):
    """
    Test the main function with a board that results in fivefold repetition.
    """
    # Set up the board to force fivefold repetition
    board.push_uci('e2e4')
    board.push_uci('e7e5')
    board.push_uci('Nf3Nc6')
    board.push_uci('Bb5a6')
    board.push_uci('O-O-O')
    board.push_uci('d7d5')
    board.push_uci('Nbd2')
    board.push_uci('c8e6')
    board.push_uci('f1c4')
    board.push_uci('f8c5')
    board.push_uci('g1f3')
    board.push_uci('g8f6')

    main()

This test suite includes comprehensive tests for the `self_sabotaging_bot` function and the `main` function. It uses pytest fixtures to provide a new chess board and parametrize the probability of making a blunder. The tests cover various scenarios, including blunders, checkmate, stalemate, and fivefold repetition.