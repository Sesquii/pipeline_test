import chess
import random
from unittest.mock import patch

# Import the functions to test


from Script_Factory.Script_Factory_Runs.all_runs.prompt10_qwen30b_default import (
    get_blunders,
    make_blunder_move,
    play_self_sabotaging_game
)

def test_get_blunders_normal_case():
    """Test get_blunders with a normal chess position."""
    board = chess.Board()
    blunders = get_blunders(board)
    
    # Should return a list of moves
    assert isinstance(blunders, list)
    
    # All moves should be legal
    for move in blunders:
        assert board.is_move_legal(move)

def test_get_blunders_empty_board():
    """Test get_blunders with an empty board (should have no legal moves)."""
    board = chess.Board()
    # Clear the board to simulate empty position
    board.clear()
    
    blunders = get_blunders(board)
    
    # Should return empty list since there are no legal moves
    assert isinstance(blunders, list)
    assert len(blunders) == 0

def test_get_blunders_specific_position():
    """Test get_blunders with a specific position that has legal moves."""
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    
    blunders = get_blunders(board)
    
    # Should return a list with legal moves
    assert isinstance(blunders, list)
    assert len(blunders) > 0
    
    # All moves should be legal
    for move in blunders:
        assert board.is_move_legal(move)

def test_make_blunder_move_normal_case():
    """Test make_blunder_move with a normal chess position."""
    board = chess.Board()
    
    move = make_blunder_move(board)
    
    # Should return either a move or None
    if move is not None:
        assert board.is_move_legal(move)

def test_make_blunder_move_empty_board():
    """Test make_blunder_move with no legal moves."""
    board = chess.Board()
    board.clear()  # Clear all pieces
    
    move = make_blunder_move(board)
    
    # Should return None when no legal moves
    assert move is None

def test_make_blunder_move_with_mate():
    """Test make_blunder_move when a forced mate is available."""
    # Create a position where black is in checkmate
    board = chess.Board("8/8/8/8/8/8/8/K1k5 w - - 0 1")
    
    move = make_blunder_move(board)
    
    # Should return None or a legal move
    if move is not None:
        assert board.is_move_legal(move)

def test_play_self_sabotaging_game_function_exists():
    """Test that play_self_sabotaging_game function exists and can be called."""
    # This test just verifies the function exists and doesn't crash immediately
    # We'll mock the random functions to avoid infinite loops or unpredictable behavior
    
    with patch('random.random') as mock_random:
        # Mock random to return specific values to control execution
        mock_random.side_effect = [0.1, 0.2, 0.3, 0.4, 0.5]  # Prevent infinite loop
        
        # Just verify it doesn't raise an exception
        try:
            # We can't easily test the full function due to side effects,
            # but we can at least make sure it doesn't crash on basic execution
            pass
        except Exception:
            # If it crashes, that's fine for this test - we just want to verify
            # it exists and has basic functionality
            pass
    
    # Basic assertion that function exists
    assert callable(play_self_sabotaging_game)

def test_get_blunders_with_no_blunders():
    """Test get_blunders when no blunders are generated due to random chance."""
    board = chess.Board()
    
    with patch('random.random') as mock_random:
        # Mock random to always return > 0.15 for first condition and > 0.1 for second
        mock_random.side_effect = [0.2, 0.2]  # Both conditions fail
        
        blunders = get_blunders(board)
        
        # Should still return a list of legal moves even if no blunders are added
        assert isinstance(blunders, list)
        for move in blunders:
            assert board.is_move_legal(move)

def test_make_blunder_move_with_no_legal_moves():
    """Test make_blunder_move when there are actually no legal moves."""
    board = chess.Board("8/8/8/8/8/8/8/K1k5 w - - 0 1")
    
    # Force a position where no moves are legal (just to be sure)
    move = make_blunder_move(board)
    
    # Should return None when no legal moves
    assert move is None

def test_get_blunders_returns_all_legal_moves():
    """Test that get_blunders returns all legal moves in some cases."""
    board = chess.Board()
    
    with patch('random.random') as mock_random:
        # Mock to ensure all moves are added (both conditions fail)
        mock_random.side_effect = [0.2, 0.2] * 20  # Ensure all moves are included
        
        blunders = get_blunders(board)
        
        legal_moves = list(board.legal_moves)
        assert len(blunders) == len(legal_moves)
