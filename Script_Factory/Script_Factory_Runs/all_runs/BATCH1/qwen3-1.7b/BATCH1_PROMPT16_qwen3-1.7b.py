```python
from typing import List

def generate_excuses(initial: str, depth: int) -> List[str]:
    """
    Generate a list of excuses where each element explains why the previous one failed.
    
    Args:
        initial: The starting excuse.
        depth: Maximum number of times to recursively generate new excuses.
        
    Returns:
        A list of strings, each explaining why the previous one failed.
    """
    if depth == 0:
        return []
    
    # Create a new excuse by appending a reason for the current one
    new_excuse = f"{initial} because I was asleep"
    return [new_excuse] + generate_excuses(new_excuse, depth - 1)

if __name__ == "__main__":
    excuselist = generate_excuses("I couldn't complete the task", 3)
    print(excuselist)