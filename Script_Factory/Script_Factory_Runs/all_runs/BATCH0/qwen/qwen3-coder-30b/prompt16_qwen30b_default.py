from typing import List

def generate_excuses(initial: str, depth: int) -> List[str]:
    """
    Generate a list of excuses where each excuse explains why the previous excuse failed.
    
    Args:
        initial: The starting excuse
        depth: The maximum recursion depth
        
    Returns:
        A list of excuses explaining why each previous excuse failed
    """
    if depth <= 0:
        return []
    
    # Base excuses that can be used to generate further excuses
    base_excuses = [
        "Because I was asleep, I couldn't set the alarm in time.",
        "Because I forgot to turn on my alarm, so I missed the meeting.",
        "Because I was running late, I couldn't prepare properly.",
        "Because I had a technical issue with my computer, I couldn't access the files.",
        "Because I misunderstood the instructions, I couldn't complete the task correctly.",
        "Because I was distracted by a phone call, I lost focus on the work.",
        "Because I was sick, I couldn't concentrate on the task.",
        "Because I had an unexpected family emergency, I couldn't finish on time."
    ]
    
    # Generate excuses recursively
    excuses = [initial]
    
    if depth > 1:
        # Pick a random excuse from base_excuses to continue the chain
        import random
        next_excuse = random.choice(base_excuses)
        # Replace the last part of the excuse with the new one
        if "I couldn't" in initial:
            # Extract the reason and create a new excuse
            reason = initial.split("I couldn't", 1)[1].strip()
            new_excuse = f"I couldn't {reason} because {next_excuse}"
        else:
            new_excuse = next_excuse
            
        # Recursively generate more excuses
        sub_excuses = generate_excuses(new_excuse, depth - 1)
        excuses.extend(sub_excuses)
    
    return excuses

if __name__ == "__main__":
    result = generate_excuses("I couldn't complete the task", 3)
    for i, excuse in enumerate(result):
        print(f"{i + 1}. {excuse}")
