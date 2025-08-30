import chess
import random

def get_blunder_moves(board):
    """Return a list of suboptimal moves that could lead to loss."""
    # Get all legal moves
    legal_moves = list(board.legal_moves)
    
    # Filter out some obvious good moves to increase chance of blunders
    blunders = []
    for move in legal_moves:
        # Avoid capturing pieces unless it's a clear advantage
        if board.is_capture(move) and board.piece_at(move.from_square).piece_type != chess.PAWN:
            # 30% chance to make a capture that loses material
            if random.random() < 0.3:
                blunders.append(move)
        else:
            # 20% chance to make a move that doesn't improve position
            if random.random() < 0.2:
                blunders.append(move)
    
    # If no blunders found, just return some moves
    if not blunders:
        return legal_moves[:min(3, len(legal_moves))]
    
    return blunders

def make_self_sabotaging_move(board):
    """Make a move that may lead to losing the game."""
    # 10% chance to try to mate opponent (but fail)
    if random.random() < 0.1:
        # Try to find a forced mate or at least a strong move
        legal_moves = list(board.legal_moves)
        return random.choice(legal_moves)
    
    # 15% chance to sacrifice material
    if random.random() < 0.15:
        legal_moves = list(board.legal_moves)
        # Try to find a move that gives up material (like moving a queen to a square where it's captured)
        for move in legal_moves:
            if board.is_capture(move) and board.piece_at(move.from_square).piece_type == chess.QUEEN:
                return move
        return random.choice(legal_moves)
    
    # 20% chance to make a blunder
    if random.random() < 0.2:
        blunders = get_blunder_moves(board)
        return random.choice(blunders)
    
    # Otherwise, make a random legal move (not necessarily bad)
    return random.choice(list(board.legal_moves))

def play_self_sabotaging_game():
    """Play a full game where the same bot plays both sides."""
    board = chess.Board()
    game = chess.pgn.Game()
    game.headers["Event"] = "Self-Sabotaging Chess Bot"
    game.headers["Site"] = "Python Script"
    game.headers["Date"] = "2023.01.01"
    game.headers["Round"] = "1"
    game.headers["White"] = "SelfSabotageBot"
    game.headers["Black"] = "SelfSabotageBot"
    
    # Keep track of moves for PGN
    node = game
    
    move_count = 0
    while not board.is_game_over():
        # Make a move
        move = make_self_sabotaging_move(board)
        
        # Add to PGN
        node = node.add_variation(move)
        
        # Play the move on the board
        board.push(move)
        move_count += 1
        
        # Occasionally force a draw by repetition or 50-move rule
        if random.random() < 0.05 and move_count > 10:
            # Try to create a position that leads to draw
            break
    
    # Determine result
    result = board.result()
    winner = "None"
    reason = ""
    
    if board.is_checkmate():
        if board.turn == chess.WHITE:
            winner = "Black"
        else:
            winner = "White"
        reason = "Checkmate"
    elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
        reason = "Draw"
    else:
        reason = "Forced move or repetition"
    
    # Print PGN
    print(game)
    
    # Print statistics
    print(f"\nStatistics:")
    print(f"Total moves played: {move_count}")
    print(f"Winner: {winner}")
    print(f"Reason for ending: {reason}")

if __name__ == "__main__":
    play_self_sabotaging_game()
