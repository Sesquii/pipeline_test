import chess
import random

def get_blunders(board):
    """Return a list of blunder moves that the bot might make."""
    # Get all legal moves
    legal_moves = list(board.legal_moves)
    
    # Filter out moves that are clearly bad or suicidal
    blunders = []
    for move in legal_moves:
        # Don't include moves that put own king in check
        if board.is_move_legal(move):
            # Occasionally sacrifice material (move to a square that loses pieces)
            if random.random() < 0.15:  # 15% chance of sacrificing
                blunders.append(move)
            elif random.random() < 0.1:  # 10% chance of forcing stalemate
                blunders.append(move)
            else:
                # Normal move, but still a blunder in some cases
                blunders.append(move)
    
    return blunders

def make_blunder_move(board):
    """Make a move that is intentionally bad."""
    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return None
    
    # Sometimes play a forced mate or stalemate move
    if random.random() < 0.05:  # 5% chance of intentional loss
        # Try to force a draw or checkmate (but not too obvious)
        for move in legal_moves:
            # Play a move that leads to stalemate or gives away checkmate
            temp_board = board.copy()
            temp_board.push(move)
            if temp_board.is_game_over():
                return move
        # If no forced game over, just return a random move
        return random.choice(legal_moves)
    
    # Most of the time, make a blunder or suboptimal move
    blunders = get_blunders(board)
    
    # Occasionally play a random move from all legal moves (for variety)
    if random.random() < 0.3:
        return random.choice(legal_moves)
    
    # Otherwise, pick from blunders
    return random.choice(blunders) if blunders else random.choice(legal_moves)

def play_self_sabotaging_game():
    """Play a full game where the bot plays both sides."""
    board = chess.Board()
    moves = []
    
    # Keep playing until game is over
    while not board.is_game_over():
        # Get current side to move
        side = "White" if board.turn == chess.WHITE else "Black"
        
        # Make a blunderous move
        move = make_blunder_move(board)
        
        if move:
            moves.append(move)
            board.push(move)
        else:
            break  # No more legal moves
            
        # Occasionally, try to force a draw or loss
        if random.random() < 0.02 and not board.is_game_over():
            # Try to force stalemate
            for m in list(board.legal_moves):
                temp_board = board.copy()
                temp_board.push(m)
                if temp_board.is_stalemate():
                    board.push(m)
                    moves.append(m)
                    break
    
    # Print final PGN
    game = chess.pgn.Game.from_board(board)
    print(game)
    
    # Statistics
    total_moves = len(moves)
    result = board.result()
    loser = "White" if board.turn == chess.WHITE else "Black"
    
    # Determine reason for loss
    reason = "blunder"
    if board.is_checkmate():
        reason = "checkmate"
    elif board.is_stalemate():
        reason = "stalemate"
    elif board.is_insufficient_material():
        reason = "insufficient material"
    elif board.is_seventyfive_moves():
        reason = "75-move rule"
    elif board.is_fivefold_repetition():
        reason = "fivefold repetition"
    
    print(f"\nStatistics:")
    print(f"Total moves: {total_moves}")
    print(f"Side that lost: {loser}")
    print(f"Reason for loss: {reason}")

if __name__ == "__main__":
    play_self_sabotaging_game()
