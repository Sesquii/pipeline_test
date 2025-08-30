import random
import json
from typing import List, Dict

# Cuisine definitions: name, typical ingredients
cuisines = {
    "Japanese": ["sushi rice", "tuna", "soy sauce", "wasabi", "nori seaweed", "pickled ginger"],
    "Italian": ["lasagna noodles", "ricotta cheese", "mozzarella", "tomato sauce", "parmesan", "basil"],
    "Mexican": ["corn tortillas", "black beans", "avocado", "cilantro", "chili peppers", "lime"],
    "Indian": ["naan bread", "curry paste", "chickpeas", "coconut milk", "cardamom", "turmeric"],
    "Egyptian": ["couscous", "tahini", "fenugreek", "eggplant", "coriander", "garlic"],
    "Thai": ["sticky rice", "pad thai sauce", "shrimp", "bean sprouts", "cucumber", "lime"],
    "Greek": ["filo pastry", "feta cheese", "olives", "lemon", "oregano", "spinach"],
    "French": ["baguette", "croissant dough", "blue cheese", "truffle oil", "shallots", "dijon mustard"],
    "Chinese": ["wonton wrappers", "hoisin sauce", "peking duck", "bamboo shoots", "star anise", "soy"],
    "Peruvian": ["quinoa", "ají amarillo paste", "plantains", "corn kernels", "cinnamon", "lime"],
    "Moroccan": ["couscous", "merguez sausage", "preserved lemons", "raisins", "coriander", "olives"]
}

def generate_absurd_recipe() -> Dict[str, str]:
    """Generate a single absurd recipe."""
    # Randomly select two different cuisines
    cuisine1, cuisine2 = random.sample(list(cuisines.keys()), 2)
    
    # Select one ingredient from each cuisine
    ing1 = random.choice(cuisines[cuisine1])
    ing2 = random.choice(cuisines[cuisine2])

    # Create a whimsical recipe name
    recipe_name = f"{cuisine1.replace(' ', '-')}-{cuisine2.replace(' ', '-')}"\
                  f" {random.choice(['Blend', 'Fusion', 'Mashup', 'Surprise'])}!"
    
    # Generate step-by-step instructions
    steps: List[str] = [
        f"- In the heart of {cuisine1}, prepare your {ing2} with a dash of {cuisine2.lower()} flair.",
        f"- Gently place your {ing1} onto layers of {cuisine2.capitalize()}, as if weaving a culinary dream.",
        f"- Infuse the essence of {cuisine1} into every bite, and let {cuisine2} be the secret whisper."
    ]
    
    return {
        "name": recipe_name,
        "ingredients": [f"* {ing1}", f"* {ing2}"],
        "instructions": steps
    }

def main() -> None:
    """Entry point to generate and print multiple absurd recipes."""
    random.seed(42)  # Ensure reproducibility

    num_recipes = 5
    all_recipes: List[Dict] = [generate_absurd_recipe() for _ in range(num_recipes)]
    
    # Output JSON to stdout
    json_output = json.dumps(all_recipes, indent=4)
    print(json_output)

if __name__ == "__main__":
    main()