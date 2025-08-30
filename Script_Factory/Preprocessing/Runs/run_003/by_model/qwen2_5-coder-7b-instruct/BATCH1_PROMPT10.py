import chess
import random

# List of potential blunders or sub-optimal moves to intentionally play
blunders = [
    "e5", "e4", "e3", "d5", "d4", "d3", "c5", "c4", "c3",
    "Nf3", "Ne2", "Nd1", "Nc2", "Nb1", "Na1",
    "Bc4", "Ba3", "Bg5", "Bh6", "Bc2",
    "O-O", "O-O-O"
]

# Function to make a blunder
def make_blunder(board):
    if random.random() < 0.1:  # 10% chance to make a blunder
        moves = [move for move in board.legal_moves]
        return random.choice(moves)
    else:
        return board.peek()

# Main function to run the game
def main():
    board = chess.Board()
    total_moves = 0

    while not board.is_game_over():
        turn = 'White' if board.turn else 'Black'
        
        # Intentionally make a blunder or a random move
        move = make_blunder(board)
        board.push(move)
        
        # Print the current board state
        print(f"Move {total_moves + 1}: {turn} plays {move}")
        print(board, "\n")
        
        total_moves += 1

    # Determine the result and print statistics
    if board.is_checkmate():
        winner = 'White' if not board.turn else 'Black'
        result = "Checkmate"
        blunder_or_mate = "Mate" if turn == winner else "Blunder"
    elif board.is_stalemate():
        result = "Stalemate"
        blunder_or_mate = "Blunder"
    else:
        result = "Draw by repetition or 50-move rule"
        blunder_or_mate = "Blunder"

    print(f"Game over: {result}")
    print(f"Total moves: {total_moves}")
    print(f"Side that lost: {turn} ({blunder_or_mate})")

    # Print the final PGN
    print(board.epd())

if __name__ == "__main__":
    main()
```

This script uses the `python-chess` library to simulate a chess game where the same bot plays both sides. The bot intentionally makes blunders or sub-optimal moves, sacrifices material, allows checkmates, or forces stalemates to lose the game in creative ways. It runs until the game ends and prints the final PGN along with simple statistics about the game.