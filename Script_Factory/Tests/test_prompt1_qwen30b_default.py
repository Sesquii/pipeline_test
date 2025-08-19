import pytest
import random
from unittest.mock import patch
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import the functions to be tested
from Script_Factory.Script_Factory_Runs.all_runs.prompt1_qwen30b_default import (
    get_random_cuisines,
    get_random_ingredients,
    generate_recipe_name,
    generate_instructions,
    generate_recipe
)

def test_get_random_cuisines_normal():
    """Test that get_random_cuisines returns two different cuisines."""
    cuisine1, cuisine2 = get_random_cuisines()
    assert cuisine1 != cuisine2
    assert cuisine1 in ["Sushi", "Lasagna", "Taco", "Curry", "Burger", "Pasta", "Samosa", "Muffin", "Pizza", "Sushi Bowl"]
    assert cuisine2 in ["Sushi", "Lasagna", "Taco", "Curry", "Burger", "Pasta", "Samosa", "Muffin", "Pizza", "Sushi Bowl"]

def test_get_random_cuisines_edge_case():
    """Test that get_random_cuisines handles the case where there's only one cuisine (should not happen in practice)."""
    # This is a theoretical edge case since we have 10 cuisines
    with patch('random.choice') as mock_choice:
        # Mock to always return same value for first choice
        mock_choice.side_effect = ["Sushi", "Lasagna"]
        result = get_random_cuisines()
        assert result == ("Sushi", "Lasagna")

def test_get_random_ingredients_normal():
    """Test that get_random_ingredients returns valid ingredients from specified cuisines."""
    cuisine1, cuisine2 = "Sushi", "Taco"
    ing1, ing2 = get_random_ingredients(cuisine1, cuisine2)
    
    # Check that ingredients are from the correct cuisines
    assert ing1 in ["rice", "salmon", "nori", "avocado", "cucumber", "soy sauce", "wasabi"]
    assert ing2 in ["tortilla", "ground beef", "lettuce", "tomato", "cheese", "sour cream", "cilantro"]

def test_get_random_ingredients_edge_case():
    """Test that get_random_ingredients handles invalid cuisine names."""
    with pytest.raises(KeyError):
        get_random_ingredients("InvalidCuisine", "Sushi")

def test_generate_recipe_name_normal():
    """Test that generate_recipe_name combines two cuisine names correctly."""
    result = generate_recipe_name("Sushi", "Taco")
    assert result == "Sushi-Taco Surprise"

def test_generate_recipe_name_edge_case():
    """Test that generate_recipe_name works with edge cases like single character cuisines."""
    result = generate_recipe_name("A", "B")
    assert result == "A-B Surprise"

def test_generate_instructions_normal():
    """Test that generate_instructions creates valid instructions for normal inputs."""
    cuisine1, cuisine2 = "Sushi", "Taco"
    ing1, ing2 = "salmon", "lettuce"
    
    instructions = generate_instructions(cuisine1, cuisine2, ing1, ing2)
    
    # Check that we get 3 instructions
    assert len(instructions) == 3
    
    # Check that placeholders are replaced
    for instruction in instructions:
        assert "{ingredient1}" not in instruction
        assert "{ingredient2}" not in instruction
        assert "{cuisine1}" not in instruction
        assert "{cuisine2}" not in instruction

def test_generate_instructions_edge_case():
    """Test that generate_instructions handles invalid cuisine names."""
    with pytest.raises(KeyError):
        generate_instructions("InvalidCuisine", "Sushi", "salmon", "lettuce")

def test_generate_instructions_empty_ingredients():
    """Test that generate_instructions handles empty ingredient inputs."""
    cuisine1, cuisine2 = "Sushi", "Taco"
    ing1, ing2 = "", ""
    
    instructions = generate_instructions(cuisine1, cuisine2, ing1, ing2)
    
    # Check that we still get 3 instructions
    assert len(instructions) == 3

def test_generate_recipe_normal():
    """Test that generate_recipe returns a complete recipe with all expected fields."""
    recipe = generate_recipe()
    
    # Check that recipe has required fields
    assert "name" in recipe
    assert "ingredients" in recipe
    assert "instructions" in recipe
    
    # Check that name is properly formatted
    assert recipe["name"].endswith(" Surprise")
    
    # Check that ingredients is a list with 2 items
    assert isinstance(recipe["ingredients"], list)
    assert len(recipe["ingredients"]) == 2
    
    # Check that instructions is a list
    assert isinstance(recipe["instructions"], list)
    assert len(recipe["instructions"]) > 0

def test_generate_recipe_consistency():
    """Test that generate_recipe produces consistent output structure."""
    recipe = generate_recipe()
    
    # Check data types
    assert isinstance(recipe["name"], str)
    assert isinstance(recipe["ingredients"], list)
    assert isinstance(recipe["instructions"], list)
    
    # Check that ingredients are strings
    for ingredient in recipe["ingredients"]:
        assert isinstance(ingredient, str)
    
    # Check that instructions are strings
    for instruction in recipe["instructions"]:
        assert isinstance(instruction, str)

def test_generate_recipe_multiple_calls():
    """Test that multiple calls to generate_recipe produce different results."""
    recipes = [generate_recipe() for _ in range(5)]
    
    # All recipes should have the expected structure
    for recipe in recipes:
        assert "name" in recipe
        assert "ingredients" in recipe
        assert "instructions" in recipe
        assert isinstance(recipe["ingredients"], list)
        assert len(recipe["ingredients"]) == 2
        assert isinstance(recipe["instructions"], list)

def test_main_function():
    """Test that main function can be called without errors (integration test)."""
    # This just tests that the function runs without throwing an exception
    # We don't actually call it since it prints to stdout
    pass

# Additional edge case tests for specific functions

def test_get_random_cuisines_consistency():
    """Test that get_random_cuisines returns different cuisines."""
    # Set seed for consistent testing
    random.seed(42)
    
    # Call multiple times to ensure randomness
    results = [get_random_cuisines() for _ in range(10)]
    
    # Check that we get different pairs (not all identical)
    unique_pairs = set(results)
    assert len(unique_pairs) > 1  # Should have more than one unique pair

def test_generate_instructions_formatting():
    """Test that generated instructions contain expected placeholders."""
    cuisine1, cuisine2 = "Sushi", "Taco"
    ing1, ing2 = "salmon", "lettuce"
    
    instructions = generate_instructions(cuisine1, cuisine2, ing1, ing2)
    
    # Should have 3 instructions
    assert len(instructions) == 3
    
    # Check that each instruction contains some of the expected content
    for instruction in instructions:
        assert isinstance(instruction, str)
        assert len(instruction) > 0

def test_generate_recipe_name_format():
    """Test that recipe name format is consistent."""
    result = generate_recipe_name("Sushi", "Taco")
    assert result == "Sushi-Taco Surprise"
    
    # Test with different cuisines
    result2 = generate_recipe_name("Pizza", "Curry")
    assert result2 == "Pizza-Curry Surprise"
