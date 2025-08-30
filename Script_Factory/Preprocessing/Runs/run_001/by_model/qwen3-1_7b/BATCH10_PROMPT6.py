```python
import sys

def generate_maze(width, height):
    """Generate a maze using recursive backtracking."""
    maze = [[True for _ in range(width)] for _ in range(height)]
    
    def dfs(x, y):
        # Mark current cell as path
        maze[x][y] = False
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < height and 0 <= ny < width and maze[nx][ny]:
                dfs(nx, ny)
    
    dfs(0, 0)
    return maze

def print_maze(maze):
    """Print the maze in a readable format."""
    for row in maze:
        line = ''
        for cell in row:
            if cell:
                line += '#'
            else:
                line += ' '
        print(line)

def main():
    width, height = 5, 5
    attempts = 0
    max_attempts = 3
    
    while True:
        print(f"Attempt {attempts + 1}")
        current_maze = generate_maze(width, height)
        print_maze(current_maze)
        
        current_x, current_y = 0, 0
        solved = False
        
        while True:
            move = input("Enter direction (U/D/L/R) or 'exit' to quit: ").strip()
            if move == 'exit':
                break
            
            # Parse the move
            dx, dy = 0, 0
            if move == 'U':
                dx = -1
            elif move == 'D':
                dx = 1
            elif move == 'L':
                dy = -1
            elif move == 'R':
                dy = 1
            else:
                print("Invalid direction")
                continue
            
            nx, ny = current_x + dx, current_y + dy
            
            if 0 <= nx < height and 0 <= ny < width and current_maze[nx][ny]:
                current_x, current_y = nx, ny
                print(f"Moved to {current_x}, {current_y}")
            
            # Check if reached the end
            if current_x == width - 1 and current_y == height - 1:
                solved = True
                break
        
        if solved:
            print("Congratulations! You solved the maze!")
            break
        
        attempts += 1
        if attempts > max_attempts:
            new_width, new_height = width + 2, height + 2
            current_maze = generate_maze(new_width, new_height)
            print("New maze generated.")
        else:
            new_width, new_height = width + 2, height + 2
            current_maze = generate_maze(new_width, new_height)
        
        print("New maze generated.")

if __name__ == "__main__":
    main()