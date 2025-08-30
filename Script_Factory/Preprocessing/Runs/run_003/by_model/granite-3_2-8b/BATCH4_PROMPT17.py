from collections import defaultdict

def venn_diagram(a, b, c):
    # Create a dictionary to store sets and intersections
    data = defaultdict(set)
    
    # Populate the sets with unique elements from each list
    for x in a:
        data[f'A'].add(x)
    for y in b:
        if y not in data['A']:
            data[f'B'].add(y)
    for z in c:
        if z not in data['A'] and z not in data['B']:
            data[f'C'].add(z)
    
    # Find intersections
    intersection_ab = data['A'] & data['B']
    intersection_ac = data['A'] & data['C']
    intersection_bc = data['B'] & data['C']
    
    unique_a = data['A'] - intersection_ab - intersection_ac
    unique_b = data['B'] - intersection_ab - intersection_bc
    unique_c = data['C'] - intersection_ac - intersection_bc

    # Print the Venn diagram
    print("Venn Diagram:")
    print("  A: ", ' '.join(str(i) for i in sorted(unique_a)))
    print("  B: ", ' '.join(str(j) for j in sorted(unique_b)))
    print("  C: ", ' '.join(str(k) for k in sorted(unique_c)))
    print("A ∩ B: ", ' '.join(str(i) for i in sorted(intersection_ab)))
    print("A ∩ C: ", ' '.join(str(j) for j in sorted(intersection_ac)))
    print("B ∩ C: ", ' '.join(str(k) for k in sorted(intersection_bc)))

if __name__ == "__main__":
    # Example usage:
    venn_diagram([1, 2, 3, 4], [3, 4, 5, 6], [7, 8, 9])