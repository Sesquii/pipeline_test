import json
import random

# Define cuisines and their ingredients
cuisines = {
    "Italian": ["tomato", "olive oil", "cheese", "bread", "pasta", "garlic", "basil"],
    "Mexican": ["avocado", "chili powder", "corn", "lime", "tortilla", "salsa", "beans"],
    "Japanese": ["rice", "fish", "soy sauce", "wasabi", "seaweed", "ginger", "eggs"],
    "Indian": ["curry powder", "spices", "chickpeas", "naan bread", "tomatoes", "cumin", "coriander"],
    "French": ["butter", "crème fraîche", "baguette", "eggs", "mushrooms", "leeks", "shallots"],
    "Spanish": ["olives", "peppers", "chili flakes", "bread", "olive oil", "tomatoes", "capers"],
    "Chinese": ["rice", "chicken", "sauce", "scallions", "ginger", "onion", "seaweed"],
    "Thai": ["coconut milk", "fish sauce", "lemongrass", "cumin", "peanuts", "crab meat", "cilantro"],
    "Turkish": ["olive oil", "pita bread", "dill", "tomatoes", "yogurt", "onions", "garlic"],
    "Vietnamese": ["rice noodles", "fish sauce", "lemon grass", "beansprouts", "lettuce", "carrots", "cilantro"]
}

def mix_cuisines():
    # Select two different cuisines
    cuisine1, cuisine2 = random.sample(list(cuisines.keys()), 2)
    
    # Select one ingredient from each cuisine
    ingredient1 = random.choice(cuisines[cuisine1])
    ingredient2 = random.choice(cuisines[cuisine2])
    
    # Create a whimsical recipe name
    recipe_name = f"{cuisine1.capitalize()}-{cuisine2.capitalize()} Surprise"
    
    # Generate step-by-step instructions
    steps = [
        f"1. Begin by preheating your oven to 350°F (175°C).",
        f"2. In a large mixing bowl, combine {ingredient1} and {ingredient2}. Stir until well mixed.",
        f"3. Take half of the mixture and shape it into a loaf on a baking sheet. Drizzle with olive oil for a golden finish.",
        f"4. Bake the loaf for 30 minutes or until golden brown. Let it cool slightly before slicing.",
        f"5. Serve slices of your {recipe_name} warm, garnished with fresh herbs if desired."
    ]
    
    # Return the recipe in JSON format
    return json.dumps({
        "Recipe Name": recipe_name,
        "Ingredients": [ingredient1, ingredient2],
        "Steps": steps
    }, indent=4)

# Generate and print five recipes
if __name__ == "__main__":
    random.seed(42)
    for _ in range(5):
        print(mix_cuisines())
        print("\n")

import json
from typing import List, Dict

# Define cuisines and their ingredients
cuisines = {
    "Italian": ["tomato", "olive oil", "cheese", "bread", "pasta", "garlic", "basil"],
    "Mexican": ["avocado", "chili powder", "corn", "lime", "tortilla", "salsa", "beans"],
    "Japanese": ["rice", "fish", "soy sauce", "wasabi", "seaweed", "ginger", "eggs"],
    "Indian": ["curry powder", "spices", "chickpeas", "naan bread", "tomatoes", "cumin", "coriander"],
    "French": ["butter", "crème fraîche", "baguette", "eggs", "mushrooms", "leeks", "shallots"],
    "Spanish": ["olives", "peppers", "chili flakes", "bread", "olive oil", "tomatoes", "capers"],
    "Chinese": ["rice", "chicken", "sauce", "scallions", "ginger", "onion", "seaweed"],
    "Thai": ["coconut milk", "fish sauce", "lemongrass", "cumin", "peanuts", "crab meat", "cilantro"],
    "Turkish": ["olive oil", "pita bread", "dill", "tomatoes", "yogurt", "onions", "garlic"],
    "Vietnamese": ["rice noodles", "fish sauce", "lemon grass", "beansprouts", "lettuce", "carrots", "cilantro"]
}

def mix_cuisines():
    # Select two different cuisines
    cuisine1, cuisine2 = random.sample(list(cuisines.keys()), 2)
    
    # Select one ingredient from each cuisine
    ingredient1 = random.choice(cuisines[cuisine1])
    ingredient2 = random.choice(cuisines[cuisine2])
    
    # Create a whimsical recipe name
    recipe_name = f"{cuisine1.capitalize()}-{cuisine2.capitalize()} Surprise"
    
    # Generate step-by-step instructions
    steps = [
        f"1. Begin by preheating your oven to 350°F (175°C).",
        f"2. In a large mixing bowl, combine {ingredient1} and {ingredient2}. Stir until well mixed.",
        f"3. Take half of the mixture and shape it into a loaf on a baking sheet. Drizzle with olive oil for a golden finish.",
        f"4. Bake the loaf for 30 minutes or until golden brown. Let it cool slightly before slicing.",
        f"5. Serve slices of your {recipe_name} warm, garnished with fresh herbs if desired."
    ]
    
    # Return the recipe in JSON format
    return json.dumps({
        "Recipe Name": recipe_name,
        "Ingredients": [ingredient1, ingredient2],
        "Steps": steps
    }, indent=4)

# Generate and print five recipes
if __name__ == "__main__":
    random.seed(42)
    for _ in range(5):
        print(mix_cuisines())
        print("\n")

# Test suite using pytest

import pytest

def test_mix_cuisines():
    """Test the mix_cuisines function."""
    result = mix_cuisines()
    data = json.loads(result)
    
    # Check if the recipe name is a string
    assert isinstance(data["Recipe Name"], str)
    
    # Check if there are exactly two ingredients in the list
    assert len(data["Ingredients"]) == 2
    
    # Check if each ingredient is a string
    for ingredient in data["Ingredients"]:
        assert isinstance(ingredient, str)
    
    # Check if there are exactly five steps in the list
    assert len(data["Steps"]) == 5
    
    # Check if each step is a string
    for step in data["Steps"]:
        assert isinstance(step, str)

def test_cuisine_pairs():
    """Test that mix_cuisines does not pair the same cuisine twice."""
    results = [mix_cuisines() for _ in range(10)]
    cuisines_used = set()
    
    for result in results:
        data = json.loads(result)
        recipe_name = data["Recipe Name"]
        
        # Extract cuisines from recipe name
        cuisine1, cuisine2 = recipe_name.split('-')
        
        # Check if both cuisines are unique and not the same
        assert cuisine1 != cuisine2
        assert (cuisine1, cuisine2) not in cuisines_used and (cuisine2, cuisine1) not in cuisines_used
        
        cuisines_used.add((cuisine1, cuisine2))

def test_randomness():
    """Test that mix_cuisines produces different results on multiple calls."""
    result1 = mix_cuisines()
    result2 = mix_cuisines()
    
    assert result1 != result2

def test_empty_cuisine_list():
    """Test the behavior when the cuisine list is empty."""
    global cuisines
    original_cuisines = cuisines.copy()
    cuisines.clear()
    
    with pytest.raises(ValueError):
        mix_cuisines()
    
    cuisines.update(original_cuisines)

def test_invalid_cuisine():
    """Test the behavior when an invalid cuisine is used."""
    global cuisines
    original_cuisines = cuisines.copy()
    cuisines["Invalid"] = []
    
    with pytest.raises(KeyError):
        mix_cuisines()
    
    cuisines.update(original_cuisines)

def test_empty_ingredient_list():
    """Test the behavior when an ingredient list is empty."""
    global cuisines
    original_cuisines = cuisines.copy()
    for cuisine in cuisines:
        cuisines[cuisine] = []
    
    with pytest.raises(ValueError):
        mix_cuisines()
    
    cuisines.update(original_cuisines)
