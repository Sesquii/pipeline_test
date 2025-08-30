import json
import random

# Seed the random generator for reproducibility
random.seed(42)

# Define cuisines and their typical ingredients
CUISINES = {
    "Italian": ["tomatoes", "pasta", "cheese", "basil", "garlic"],
    "Japanese": ["sushi rice", "nori sheets", "raw fish", "soy sauce", "wasabi"],
    "Mexican": ["tortillas", "beans", "chili peppers", "avocado", "lime"],
    "French": ["butter", "wine", "herbs", "cream", "baguette"],
    "Indian": ["curry powder", "rice", "naan bread", "chickpeas", "coconut milk"],
    "American": ["hamburger", "fries", "ketchup", "mustard", "bbq sauce"],
    "Chinese": ["soy sauce", "noodles", "tofu", "ginger", "sesame oil"],
    "Thai": ["coconut milk", "lime leaves", "chili peppers", "fish sauce", "rice noodles"],
    "Greek": ["olives", "feta cheese", "tzatziki", "pita bread", "ouzo"],
    "Spanish": ["paella rice", "chorizo", "saffron", "olive oil", "garlic"]
}

def get_cuisine_pairs():
    """Generate all possible pairs of cuisines"""
    cuisine_names = list(CUISINES.keys())
    pairs = []
    for i in range(len(cuisine_names)):
        for j in range(i + 1, len(cuisine_names)):
            pairs.append((cuisine_names[i], cuisine_names[j]))
    return pairs

def generate_recipe_name(cuisine1, cuisine2):
    """Create a whimsical recipe name from two cuisines"""
    return f"{cuisine1}-{cuisine2} Fusion"

def generate_ingredients(cuisine1, cuisine2):
    """Select one ingredient from each cuisine and combine them"""
    ingredients = []
    ingredients.extend(random.sample(CUISINES[cuisine1], 1))
    ingredients.extend(random.sample(CUISINES[cuisine2], 1))
    return ingredients

def generate_instructions(cuisine1, cuisine2):
    """Generate humorous step-by-step instructions mixing both cuisines"""
    instructions = [
        f"1. Begin by preparing your {cuisine1.lower()} base. Make sure to add a dash of {random.choice(CUISINES[cuisine2])} for that extra {cuisine2.lower()} twist!",
        f"2. While your base is cooking, chop up some {random.choice(CUISINES[cuisine1])} and marinate it in {random.choice(CUISINES[cuisine2])} juice.",
        f"3. Assemble your dish by layering the {cuisine1.lower()} base with the marinated {cuisine1.lower()} chunks, then top it off with a generous helping of {random.choice(CUISINES[cuisine2])}.",
        f"4. Bake in a preheated oven at 375°F (190°C) for about 20-25 minutes, or until the {cuisine2.lower()} topping starts to bubble and brown.",
        f"5. Serve hot with a side of {random.choice(CUISINES[cuisine1])} salad drizzled with {random.choice(CUISINES[cuisine2])} dressing."
    ]
    return instructions

def generate_recipe(cuisine1, cuisine2):
    """Generate a complete recipe object"""
    recipe_name = generate_recipe_name(cuisine1, cuisine2)
    ingredients = generate_ingredients(cuisine1, cuisine2)
    instructions = generate_instructions(cuisine1, cuisine2)

    return {
        "recipe_name": recipe_name,
        "cuisines": [cuisine1, cuisine2],
        "ingredients": ingredients,
        "instructions": instructions
    }

def main():
    """Main function to generate and output recipes"""
    # Get all possible cuisine pairs
    cuisine_pairs = get_cuisine_pairs()

    # Shuffle pairs for randomness (though we've seeded, this adds variety)
    random.shuffle(cuisine_pairs)

    # Generate 5 recipes
    recipes = []
    for i in range(5):
        cuisine1, cuisine2 = cuisine_pairs[i]
        recipe = generate_recipe(cuisine1, cuisine2)
        recipes.append(recipe)

    # Output as JSON
    print(json.dumps(recipes, indent=2))

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====

import pytest
from typing import List, Tuple

# Original code remains unchanged

def test_get_cuisine_pairs():
    """Test the get_cuisine_pairs function"""
    pairs = get_cuisine_pairs()
    assert len(pairs) == 45  # There are 10 cuisines, so 45 unique pairs
    for pair in pairs:
        assert isinstance(pair, tuple)
        assert len(pair) == 2
        assert all(isinstance(cuisine, str) for cuisine in pair)

def test_generate_recipe_name():
    """Test the generate_recipe_name function"""
    cuisine1 = "Italian"
    cuisine2 = "Japanese"
    recipe_name = generate_recipe_name(cuisine1, cuisine2)
    assert isinstance(recipe_name, str)
    assert f"{cuisine1}-{cuisine2} Fusion" in recipe_name

def test_generate_ingredients():
    """Test the generate_ingredients function"""
    cuisine1 = "Italian"
    cuisine2 = "Japanese"
    ingredients = generate_ingredients(cuisine1, cuisine2)
    assert isinstance(ingredients, list)
    assert len(ingredients) == 2
    assert all(isinstance(ingredient, str) for ingredient in ingredients)

def test_generate_instructions():
    """Test the generate_instructions function"""
    cuisine1 = "Italian"
    cuisine2 = "Japanese"
    instructions = generate_instructions(cuisine1, cuisine2)
    assert isinstance(instructions, list)
    assert len(instructions) == 5
    assert all(isinstance(instruction, str) for instruction in instructions)

def test_generate_recipe():
    """Test the generate_recipe function"""
    cuisine1 = "Italian"
    cuisine2 = "Japanese"
    recipe = generate_recipe(cuisine1, cuisine2)
    assert isinstance(recipe, dict)
    assert "recipe_name" in recipe
    assert "cuisines" in recipe
    assert "ingredients" in recipe
    assert "instructions" in recipe
    assert len(recipe["cuisines"]) == 2
    assert all(isinstance(cuisine, str) for cuisine in recipe["cuisines"])
    assert isinstance(recipe["ingredients"], list)
    assert len(recipe["ingredients"]) == 2
    assert all(isinstance(ingredient, str) for ingredient in recipe["ingredients"])
    assert isinstance(recipe["instructions"], list)
    assert len(recipe["instructions"]) == 5
    assert all(isinstance(instruction, str) for instruction in recipe["instructions"])

def test_main():
    """Test the main function"""
    # Capture the output of the main function
    with pytest.raises(SystemExit):
        main()

# Test cases using fixtures and parametrization
@pytest.fixture(params=["Italian", "Japanese", "Mexican", "French", "Indian", "American", "Chinese", "Thai", "Greek", "Spanish"])
def cuisine(request):
    return request.param

def test_cuisine_pairs(cuisine):
    """Test the get_cuisine_pairs function with different cuisines"""
    pairs = get_cuisine_pairs()
    assert len(pairs) == 45
    for pair in pairs:
        assert isinstance(pair, tuple)
        assert len(pair) == 2
        assert all(isinstance(cuisine, str) for cuisine in pair)

def test_generate_recipe_with_cuisine(cuisine):
    """Test the generate_recipe function with different cuisines"""
    cuisine1 = cuisine
    cuisine2 = "Japanese" if cuisine != "Japanese" else "Italian"
    recipe = generate_recipe(cuisine1, cuisine2)
    assert isinstance(recipe, dict)
    assert "recipe_name" in recipe
    assert "cuisines" in recipe
    assert "ingredients" in recipe
    assert "instructions" in recipe
    assert len(recipe["cuisines"]) == 2
    assert all(isinstance(cuisine, str) for cuisine in recipe["cuisines"])
    assert isinstance(recipe["ingredients"], list)
    assert len(recipe["ingredients"]) == 2
    assert all(isinstance(ingredient, str) for ingredient in recipe["ingredients"])
    assert isinstance(recipe["instructions"], list)
    assert len(recipe["instructions"]) == 5
    assert all(isinstance(instruction, str) for instruction in recipe["instructions"])

# Test cases with negative scenarios
def test_generate_recipe_with_invalid_cuisine():
    """Test the generate_recipe function with invalid cuisine"""
    cuisine1 = "InvalidCuisine"
    cuisine2 = "Japanese"
    with pytest.raises(KeyError):
        generate_recipe(cuisine1, cuisine2)

def test_generate_recipe_with_empty_cuisine():
    """Test the generate_recipe function with empty cuisine"""
    cuisine1 = ""
    cuisine2 = "Japanese"
    with pytest.raises(ValueError):
        generate_recipe(cuisine1, cuisine2)
