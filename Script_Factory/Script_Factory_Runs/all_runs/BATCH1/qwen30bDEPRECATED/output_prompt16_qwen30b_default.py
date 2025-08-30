from typing import List

def generate_excuses(initial: str, depth: int) -> List[str]:
    """
    Generate a list of excuses where each excuse explains why the previous one failed.
    
    Args:
        initial: The starting excuse
        depth: The maximum depth of recursion
        
    Returns:
        A list of excuses, with each explaining why the previous one failed
    """
    if depth <= 0:
        return []
    
    # Base excuses that can be used to generate more excuses
    base_excuses = [
        "I forgot to turn on my alarm, so I missed the meeting.",
        "Because I was asleep, I couldn't set the alarm in time.",
        "The internet was down, so I couldn't access the system.",
        "My computer crashed, so I lost all my work.",
        "I had a family emergency and couldn't focus on the task.",
        "The deadline was moved up unexpectedly, leaving no time to prepare.",
        "I misunderstood the requirements and started working in the wrong direction.",
        "There was a power outage during the critical phase of completion."
    ]
    
    # Generate the first excuse
    excuses = [initial]
    
    # Recursively generate more excuses
    def _generate_more(current_excuse: str, remaining_depth: int) -> List[str]:
        if remaining_depth <= 0:
            return []
        
        # Simple rule to determine which excuse to use next
        # We'll just pick the first excuse from our list that hasn't been used yet
        # In a more complex version, we might use some logic to match with the current excuse
        next_excuse = base_excuses[len(excuses) % len(base_excuses)]
        
        # Create a logical explanation for why this excuse failed
        explanation = f"Because {current_excuse.split(',')[0].lower()}, I couldn't fulfill the task."
        
        return [explanation] + _generate_more(explanation, remaining_depth - 1)
    
    # Add recursive excuses
    additional_excuses = _generate_more(initial, depth - 1)
    
    return excuses + additional_excuses

if __name__ == "__main__":
    result = generate_excuses("I couldn't complete the task", 3)
    for i, excuse in enumerate(result):
        print(f"{i+1}. {excuse}")
