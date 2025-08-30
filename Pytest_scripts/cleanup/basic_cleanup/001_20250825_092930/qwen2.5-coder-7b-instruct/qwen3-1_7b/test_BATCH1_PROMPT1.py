
import random
import json

random.seed(42)

cuisines = {
    "Japanese": ["rice", "fish", "soy sauce", "sesame seeds", "dashi"],
    "Italian": ["pasta", "olive oil", "tomatoes", "basil", "parmesan cheese"],
    "Mexican": ["tortillas", "chili", "cabbage", "cheese", "salsa"],
    "Korean": ["kimchi", "kimchi sauce", "spring rolls", "rice", "gochujang"],
    "Chinese": ["noodles", "soy sauce", "tofu", "sesame seeds", "miso"],
    "Indian": ["curry powder", "spices", "dal", "lentils", "saffron"],
    "Thai": ["tamarind", "chili", "lemon", "papaya", "lime"],
    "French": ["bread", "butter", "cheese", "mushrooms", "herbs"],
    "German": ["rye bread", "ketchup", "sauerkraut", "gravy", "couscous"],
    "Middle Eastern": ["pita", "tomato sauce", "sesame seeds", "sumac", "basil"]
}

def generate_recipe(cuisine1, cuisine2):
    """Generate a whimsical cooking recipe by blending two cuisines."""
    # Select one ingredient from each cuisine
    ing1 = random.choice(cuisines[cuisine1])
    ing2 = random.choice(cuisines[cuisine2])
    
    # Create a whimsical recipe name combining the two cuisines
    recipe_name = f"{cuisine1}-{cuisine2} Surprise"
    
    # Generate humorous steps that mix cooking techniques and cultural references
    steps = []
    steps.append(f"1. {ing1} and {ing2} are combined in a pot, using {random.choice(['a wok', 'a knife', 'a rice cooker'])}.")
    steps.append(f"2. Use a {random.choice(['Japanese technique', 'Italian method'])} to mix the ingredients.")
    steps.append(f"3. The mixture is then cooked in a {random.choice(['French oven', 'German pan'])}.")
    
    return {
        "name": recipe_name,
        "ingredients": [ing1, ing2],
        "steps": steps
    }

def main():
    """Main function to generate and output five absurd recipes."""
    recipes = []
    # Generate 5 unique pairs of cuisines
    for _ in range(5):
        cuisine1 = random.choice(list(cuisines.keys()))
        cuisine2 = random.choice([cuisine for cuisine in list(cuisines.keys()) if cuisine != cuisine1])
        recipe = generate_recipe(cuisine1, cuisine2)
        recipes.append(recipe)
    
    # Convert the list of recipes to JSON format and print
    json_output = json.dumps(recipes, indent=4)
    print(json_output)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====

import pytest
from typing import Dict, List

# Original code remains unchanged

def test_generate_recipe():
    """Test the generate_recipe function with different cuisines."""
    # Positive test case: Valid cuisine inputs
    recipe = generate_recipe("Japanese", "Italian")
    assert isinstance(recipe, dict)
    assert "name" in recipe and isinstance(recipe["name"], str)
    assert "ingredients" in recipe and isinstance(recipe["ingredients"], list) and len(recipe["ingredients"]) == 2
    assert "steps" in recipe and isinstance(recipe["steps"], list) and len(recipe["steps"]) == 3
    
    # Negative test case: Invalid cuisine input
    with pytest.raises(KeyError):
        generate_recipe("Japanese", "InvalidCuisine")

def test_main():
    """Test the main function to ensure it generates five unique recipes."""
    # Positive test case: Check if main function outputs JSON
    from io import StringIO
    import sys
    
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    
    main()
    
    sys.stdout = old_stdout
    json_output = mystdout.getvalue()
    
    assert isinstance(json_output, str)
    recipes = json.loads(json_output)
    assert len(recipes) == 5
    
    # Check if all recipes are unique
    recipe_names = [recipe["name"] for recipe in recipes]
    assert len(recipe_names) == len(set(recipe_names))
    
    # Check if each recipe has the correct structure
    for recipe in recipes:
        assert "name" in recipe and isinstance(recipe["name"], str)
        assert "ingredients" in recipe and isinstance(recipe["ingredients"], list) and len(recipe["ingredients"]) == 2
        assert "steps" in recipe and isinstance(recipe["steps"], list) and len(recipe["steps"]) == 3

# Add more test cases as needed
