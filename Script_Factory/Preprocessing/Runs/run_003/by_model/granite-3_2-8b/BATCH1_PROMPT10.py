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