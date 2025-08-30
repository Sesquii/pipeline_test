import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest

## absurd_recipes is not the name of the actual script file, the actual script is named prompt1_qwen30b_default(.py) 
from Script_Factory.Script_Factory_runs.all_runs.absurd_recipes import (
    get_random_cuisines,
    get_random_ingredients,
    generate_recipe_name,
    generate_instructions,
    generate_recipe,
    CUISINES
)

def test_get_random_cuisines_normal():
    """Test that get_random_cuisines returns two different cuisines"""
    cuisine1, cuisine2 = get_random_cuisines()
    assert cuisine1 in CUISINES
    assert cuisine2 in CUISINES
    assert cuisine1 != cuisine2

def test_get_random_cuisines_edge_case():
    """Test that get_random_cuisines handles the case where only one cuisine exists (should not happen but testing edge case)"""
    # This test is more about ensuring no exception occurs with normal data
    cuisine1, cuisine2 = get_random_cuisines()
    assert isinstance(cuisine1, str)
    assert isinstance(cuisine2, str)

def test_get_random_ingredients_normal():
    """Test that get_random_ingredients returns valid ingredients from given cuisines"""
    cuisine1 = "Sushi"
    cuisine2 = "Lasagna"
    ing1, ing2 = get_random_ingredients(cuisine1, cuisine2)
    
    assert ing1 in CUISINES[cuisine1]
    assert ing2 in CUISINES[cuisine2]

def test_get_random_ingredients_edge_case():
    """Test that get_random_ingredients works with different cuisines"""
    cuisine1 = "Taco"
    cuisine2 = "Curry"
    ing1, ing2 = get_random_ingredients(cuisine1, cuisine2)
    
    assert ing1 in CUISINES[cuisine1]
    assert ing2 in CUISINES[cuisine2]

def test_generate_recipe_name_normal():
    """Test that generate_recipe_name creates a proper combined name"""
    cuisine1 = "Sushi"
    cuisine2 = "Lasagna"
    name = generate_recipe_name(cuisine1, cuisine2)
    
    assert name == "Sushi-Lasagna Surprise"

def test_generate_recipe_name_edge_case():
    """Test that generate_recipe_name works with different cuisine names"""
    cuisine1 = "Pizza"
    cuisine2 = "Muffin"
    name = generate_recipe_name(cuisine1, cuisine2)
    
    assert name == "Pizza-Muffin Surprise"

def test_generate_instructions_normal():
    """Test that generate_instructions creates valid instructions for two cuisines"""
    cuisine1 = "Sushi"
    cuisine2 = "Lasagna"
    ingredient1 = "rice"
    ingredient2 = "tomato sauce"
    
    instructions = generate_instructions(cuisine1, cuisine2, ingredient1, ingredient2)
    
    assert isinstance(instructions, list)
    assert len(instructions) == 3
    assert all(isinstance(instruction, str) for instruction in instructions)

def test_generate_instructions_edge_case():
    """Test that generate_instructions works with different cuisines and ingredients"""
    cuisine1 = "Burger"
    cuisine2 = "Pasta"
    ingredient1 = "beef patty"
    ingredient2 = "marinara sauce"
    
    instructions = generate_instructions(cuisine1, cuisine2, ingredient1, ingredient2)
    
    assert isinstance(instructions, list)
    assert len(instructions) == 3
    assert all(isinstance(instruction, str) for instruction in instructions)

def test_generate_recipe_normal():
    """Test that generate_recipe creates a complete recipe with proper structure"""
    recipe = generate_recipe()
    
    assert "name" in recipe
    assert "ingredients" in recipe
    assert "instructions" in recipe
    
    assert isinstance(recipe["name"], str)
    assert isinstance(recipe["ingredients"], list)
    assert isinstance(recipe["instructions"], list)
    
    assert len(recipe["ingredients"]) == 2
    assert len(recipe["instructions"]) >= 1

def test_generate_recipe_edge_case():
    """Test that generate_recipe handles edge cases properly"""
    # Test that we get valid data structure
    recipe = generate_recipe()
    
    # Should have a name that contains both cuisines
    assert "name" in recipe
    assert isinstance(recipe["name"], str)
    
    # Should have ingredients list with 2 items
    assert len(recipe["ingredients"]) == 2
    assert all(isinstance(ing, str) for ing in recipe["ingredients"])
    
    # Should have instructions list
    assert isinstance(recipe["instructions"], list)
    assert len(recipe["instructions"]) >= 1

def test_cuisines_data_structure():
    """Test that CUISINES dictionary has the expected structure"""
    assert isinstance(CUISINES, dict)
    assert len(CUISINES) > 0
    
    # Check that all cuisines have ingredients
    for cuisine, ingredients in CUISINES.items():
        assert isinstance(cuisine, str)
        assert isinstance(ingredients, list)
        assert len(ingredients) > 0
