git import random
import json

# Set seed for reproducibility
random.seed(42)

# Define cuisines and their typical ingredients
CUISINES = {
    "Sushi": ["rice", "salmon", "nori", "avocado", "cucumber", "soy sauce", "wasabi"],
    "Lasagna": ["pasta", "tomato sauce", "cheese", "beef", "eggplant", "basil", "garlic"],
    "Taco": ["tortilla", "ground beef", "lettuce", "tomato", "cheese", "sour cream", "cilantro"],
    "Curry": ["rice", "chicken", "coconut milk", "curry paste", "onion", "garlic", "ginger"],
    "Burger": ["bun", "beef patty", "lettuce", "tomato", "cheese", "pickle", "ketchup"],
    "Pasta": ["pasta", "marinara sauce", "basil", "garlic", "olive oil", "parmesan", "meatballs"],
    "Samosa": ["pastry", "potatoes", "peas", "onion", "spices", "ginger", "cumin"],
    "Muffin": ["flour", "butter", "sugar", "eggs", "milk", "blueberries", "vanilla"],
    "Pizza": ["dough", "tomato sauce", "cheese", "pepperoni", "mushrooms", "olives", "basil"],
    "Sushi Bowl": ["rice", "tuna", "seaweed", "sriracha", "cucumber", "carrot", "sesame oil"]
}

def get_random_cuisines():
    """Randomly select two different cuisines from the CUISINES dictionary."""
    cuisines = list(CUISINES.keys())
    first = random.choice(cuisines)
    second = random.choice([c for c in cuisines if c != first])
    return first, second

def get_random_ingredients(cuisine1, cuisine2):
    """Select one ingredient from each of the two given cuisines."""
    ing1 = random.choice(CUISINES[cuisine1])
    ing2 = random.choice(CUISINES[cuisine2])
    return ing1, ing2

def generate_recipe_name(cuisine1, cuisine2):
    """Create a whimsical recipe name by combining the names of two cuisines."""
    return f"{cuisine1}-{cuisine2} Surprise"

def generate_instructions(cuisine1, cuisine2, ingredient1, ingredient2):
    """
    Generate humorous step-by-step cooking instructions that blend techniques
    and cultural references from both cuisines.
    """
    # Define typical steps for each cuisine
    steps = {
        "Sushi": [
            "Roll the {ingredient1} in a {ingredient2}-infused {cuisine2} wrap.",
            "Slice into thin pieces with a {cuisine2} blade.",
            "Serve on a bed of {cuisine1} rice."
        ],
        "Lasagna": [
            "Layer the {ingredient1} with {ingredient2} in a {cuisine2} dish.",
            "Bake until the {cuisine1} mixture bubbles.",
            "Top with {cuisine2} cheese and serve hot."
        ],
        "Taco": [
            "Warm the {cuisine2} tortillas on a {cuisine1} skillet.",
            "Fill with {ingredient1} seasoned like a {cuisine2} dish.",
            "Garnish with {ingredient2} and enjoy."
        ],
        "Curry": [
            "Cook {ingredient1} in {cuisine2} coconut milk for 15 minutes.",
            "Add {ingredient2} and stir with a {cuisine1} spatula.",
            "Serve over {cuisine2} rice with {cuisine1} naan."
        ],
        "Burger": [
            "Form the {ingredient1} into a {cuisine1} patty.",
            "Grill until it's {cuisine2} brown.",
            "Place on a {cuisine2} bun with {ingredient2}."
        ],
        "Pasta": [
            "Boil the {cuisine1} pasta for 8 minutes.",
            "Mix in {ingredient1} sauce from {cuisine2}.",
            "Top with {ingredient2} and fresh {cuisine2} basil."
        ],
        "Samosa": [
            "Fill the {cuisine1} pastry with {ingredient1} and {ingredient2}.",
            "Deep-fry until it's crispy like a {cuisine2} dish.",
            "Serve with {cuisine2} chutney."
        ],
        "Muffin": [
            "Mix {ingredient1} into the {cuisine2} batter.",
            "Bake in a {cuisine1} muffin tin for 20 minutes.",
            "Top with {ingredient2} glaze."
        ],
        "Pizza": [
            "Spread {ingredient1} sauce on the {cuisine2} crust.",
            "Add {ingredient2} and bake until {cuisine1} bubbly.",
            "Finish with {cuisine2} herbs before serving."
        ],
        "Sushi Bowl": [
            "Layer {ingredient1} over {cuisine2} rice.",
            "Drizzle with {cuisine1} sauce and {ingredient2}.",
            "Garnish with {cuisine2} sesame seeds."
        ]
    }
    
    # Get a random set of instructions for each cuisine
    steps1 = random.choice(steps[cuisine1])
    steps2 = random.choice(steps[cuisine2])
    steps3 = random.choice([
        "Serve with a side of {cuisine1} {ingredient2}.",
        "Add {ingredient1} to complete the {cuisine2} experience.",
        "Finish with {cuisine1} spices for an extra {cuisine2} kick."
    ])
    
    # Replace placeholders in steps
    instructions = [
        steps1.format(ingredient1=ingredient1, ingredient2=ingredient2, cuisine1=cuisine1, cuisine2=cuisine2),
        steps2.format(ingredient1=ingredient1, ingredient2=ingredient2, cuisine1=cuisine1, cuisine2=cuisine2),
        steps3.format(ingredient1=ingredient1, ingredient2=ingredient2, cuisine1=cuisine1, cuisine2=cuisine2)
    ]
    
    return instructions

def generate_recipe():
    """Generate a single absurd recipe by combining two cuisines."""
    # Select two different cuisines
    cuisine1, cuisine2 = get_random_cuisines()
    
    # Select one ingredient from each
    ingredient1, ingredient2 = get_random_ingredients(cuisine1, cuisine2)
    
    # Create recipe name
    name = generate_recipe_name(cuisine1, cuisine2)
    
    # Generate instructions
    instructions = generate_instructions(cuisine1, cuisine2, ingredient1, ingredient2)
    
    return {
        "name": name,
        "ingredients": [ingredient1, ingredient2],
        "instructions": instructions
    }

def main():
    """Generate and output five absurd recipes in JSON format."""
    recipes = []
    for _ in range(5):
        recipe = generate_recipe()
        recipes.append(recipe)
    
    # Output as JSON
    print(json.dumps(recipes, indent=2))

if __name__ == "__main__":
    main()
