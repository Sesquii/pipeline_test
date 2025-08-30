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