import random
import json

# Set seed for reproducibility
random.seed(42)

def define_cuisines():
    """
    Define at least 10 distinct cuisines with typical ingredients.
    Each cuisine is represented as a dictionary entry with name and ingredient list.
    """
    cuisines = {
        "Sushi": ["rice", "tuna", "seaweed", "avocado", "soy sauce", "wasabi", "ginger"],
        "Lasagna": ["pasta", "beef", "tomato sauce", "cheese", "noodles", "ricotta", "basil"],
        "Tacos": ["tortilla", "beef", "lettuce", "cheese", "sour cream", "tomatoes", "onions"],
        "Curry": ["rice", "chicken", "coconut milk", "curry paste", "onions", "garlic", "ginger"],
        "Pizza": ["dough", "tomato sauce", "cheese", "pepperoni", "mushrooms", "olives", "basil"],
        "Burger": ["bun", "beef patty", "lettuce", "tomato", "cheese", "pickles", "ketchup"],
        "Pasta": ["pasta", "tomato sauce", "basil", "garlic", "olive oil", "parmesan", "meatballs"],
        "Sushi Rolls": ["rice", "nori", "cucumber", "carrot", "avocado", "spicy mayo", "sriracha"],
        "Falafel": ["chickpeas", "parsley", "garlic", "onion", "cumin", "coriander", "pita bread"],
        "Ramen": ["noodles", "broth", "pork", "egg", "bamboo shoots", "green onions", "soy sauce"]
    }
    return cuisines

def pair_cuisines(cuisines):
    """
    Randomly select two different cuisines from the list.
    Returns a tuple of two cuisine names.
    """
    keys = list(cuisines.keys())
    first = random.choice(keys)
    second = random.choice([k for k in keys if k != first])
    return (first, second)

def combine_ingredients(cuisine1, cuisine2, cuisines):
    """
    Select one ingredient from each of two cuisines and combine them into a list.
    Returns a list of combined ingredients.
    """
    ing1 = random.choice(cuisines[cuisine1])
    ing2 = random.choice(cuisines[cuisine2])
    return [ing1, ing2]

def generate_recipe_name(cuisine1, cuisine2):
    """
    Create a whimsical recipe name by blending the two cuisine names.
    Returns a string with the combined name.
    """
    # Split and take first part of each cuisine name for blending
    name1 = cuisine1.split()[0] if " " in cuisine1 else cuisine1
    name2 = cuisine2.split()[0] if " " in cuisine2 else cuisine2
    return f"{name1}-{name2} Surprise"

def generate_instructions(cuisine1, cuisine2, ingredients):
    """
    Generate humorous step-by-step cooking instructions that blend techniques from both cuisines.
    Returns a list of instruction strings.
    """
    # Get first ingredient as the main item for the dish
    main_item = ingredients[0]
    
    # Define technique templates for each cuisine
    techniques = {
        "Sushi": ["roll", "slice", "season", "marinate"],
        "Lasagna": ["layer", "bake", "simmer", "assemble"],
        "Tacos": ["fill", "grill", "sauce", "wrap"],
        "Curry": ["stir", "spice", "simmer", "serve"],
        "Pizza": ["top", "bake", "stretch", "add"],
        "Burger": ["grill", "assemble", "season", "serve"],
        "Pasta": ["boil", "sauce", "mix", "toss"],
        "Sushi Rolls": ["roll", "slice", "season", "garnish"],
        "Falafel": ["form", "fry", "season", "serve"],
        "Ramen": ["boil", "add", "season", "serve"]
    }
    
    # Get random techniques from both cuisines
    tech1 = random.choice(techniques.get(cuisine1, ["cook"]))
    tech2 = random.choice(techniques.get(cuisine2, ["cook"]))
    
    # Create funny instructions
    instructions = [
        f"Begin by {tech1}ing the {main_item}.",
        f"Next, {tech2} the second ingredient in a separate pan.",
        "Combine both ingredients with a pinch of creativity and a dash of absurdity.",
        "Serve on a plate that looks like it belongs in a different country.",
        "Enjoy your culinary adventure that defies all logic and taste expectations!"
    ]
    
    return instructions

def generate_recipe(cuisines):
    """
    Generate a single recipe by pairing cuisines, selecting ingredients, 
    creating a name, and generating instructions.
    Returns a dictionary representing one recipe.
    """
    # Pair two cuisines
    c1, c2 = pair_cuisines(cuisines)
    
    # Combine ingredients from both cuisines
    ingredients = combine_ingredients(c1, c2, cuisines)
    
    # Create recipe name
    name = generate_recipe_name(c1, c2)
    
    # Generate instructions
    instructions = generate_instructions(c1, c2, ingredients)
    
    return {
        "recipe_name": name,
        "cuisines": [c1, c2],
        "ingredients": ingredients,
        "instructions": instructions
    }

def main():
    """
    Main function to generate and output five absurd recipes in JSON format.
    """
    # Define all cuisines with their typical ingredients
    cuisines = define_cuisines()
    
    # Generate 5 recipes
    recipes = []
    for _ in range(5):
        recipe = generate_recipe(cuisines)
        recipes.append(recipe)
    
    # Output as JSON
    print(json.dumps(recipes, indent=2))

if __name__ == "__main__":
    main()
