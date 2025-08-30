import random
import sys

# Function to generate recursive art
def generative_art(depth):
    # Base case: if depth is 0, return a simple shape or symbol
    if depth == 0:
        return "*"
    
    # Recursive case: create a more complex pattern
    result = []
    for _ in range(3):  # Create 3 levels of recursion
        new_depth = depth - 1
        sub_art = generative_art(new_depth)
        
        # Apply some randomness and transformation to the sub-art
        if random.choice([True, False]):
            sub_art = sub_art.replace("*", "#")
        elif random.choice([True, False]):
            sub_art += " "
        
        result.append(sub_art)
    
    return "\n".join(result)

# Main entry point of the program
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generative_art_bot.py <depth>")
        sys.exit(1)
    
    depth = int(sys.argv[1])
    art = generative_art(depth)
    print(art)
```

This Python script defines a recursive function `generative_art` that generates complex and unpredictable text-based "art" based on the input depth. The script takes a single command-line argument representing the depth of recursion. The base case returns a simple "*", and the recursive case creates more intricate patterns by combining simpler ones with randomness in symbols and spacing. The main entry point checks for the correct number of arguments, calls the `generative_art` function with the provided depth, and prints the resulting art.