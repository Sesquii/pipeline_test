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

# ===== GENERATED TESTS =====

import pytest
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

# Test suite

def test_generate_absurd_recipe():
    """Test the generate_absurd_recipe function."""
    recipe = generate_absurd_recipe()
    
    assert isinstance(recipe, dict)
    assert "name" in recipe
    assert "ingredients" in recipe
    assert "instructions" in recipe
    
    # Check if ingredients are from different cuisines
    ingredient1, ingredient2 = recipe["ingredients"]
    cuisine1 = next((key for key, value in cuisines.items() if ingredient1.strip('* ') in value), None)
    cuisine2 = next((key for key, value in cuisines.items() if ingredient2.strip('* ') in value), None)
    
    assert cuisine1 is not None
    assert cuisine2 is not None
    assert cuisine1 != cuisine2
    
    # Check if instructions are a list of strings
    assert isinstance(recipe["instructions"], list)
    for step in recipe["instructions"]:
        assert isinstance(step, str)

def test_main():
    """Test the main function."""
    with pytest.raises(SystemExit) as e:
        main()
    
    assert e.type == SystemExit
    assert e.value.code == 0

def test_generate_absurd_recipe_with_fixed_cuisines():
    """Test the generate_absurd_recipe function with fixed cuisines."""
    random.seed(42)
    
    recipe = generate_absurd_recipe()
    
    # Check if ingredients are from different cuisines
    ingredient1, ingredient2 = recipe["ingredients"]
    cuisine1 = next((key for key, value in cuisines.items() if ingredient1.strip('* ') in value), None)
    cuisine2 = next((key for key, value in cuisines.items() if ingredient2.strip('* ') in value), None)
    
    assert cuisine1 is not None
    assert cuisine2 is not None
    assert cuisine1 != cuisine2
    
    # Check if instructions are a list of strings
    assert isinstance(recipe["instructions"], list)
    for step in recipe["instructions"]:
        assert isinstance(step, str)

def test_generate_absurd_recipe_with_empty_cuisines():
    """Test the generate_absurd_recipe function with empty cuisines."""
    global cuisines
    cuisines = {}
    
    with pytest.raises(ValueError):
        generate_absurd_recipe()

    # Restore original cuisines
    global cuisines
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
