```python
import random
from python_chess import Game

def main():
    # Initialize chess game
    game = Game()
    total_moves = 0
    side_lost = None
    forced_mate = False

    # List of suboptimal or blunder moves
    blunders = ["e5", "d4", "c6"]  # Example bad moves for the bot to choose from

    while not game.is_over():
        if game.turn == chess.WHITE:
            move = random.choice(blunders)
            game.make_move(move)
            total_moves += 1
            if game.is_checkmate():
                side_lost = "white"
                forced_mate = True
                break
        else:
            move = random.choice(blunders)
            game.make_move(move)
            total_moves += 1
            if game.is_checkmate():
                side_lost = "black"
                forced_mate = True
                break

    # Print the final PGN and statistics
    print("PGN:")
    print(game.to_pgn())
    print(f"Total moves: {total_moves}")
    if forced_mate:
        print("Loss was a forced mate.")
    else:
        print("Loss was a blunder.")

if __name__ == "__main__":
    main()