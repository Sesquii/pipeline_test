import json
import random

def corrupt_key_value(value):
    if isinstance(value, (int, float)):
        return str(value)  # Change number to string
    elif isinstance(value, bool):
        return None       # Change boolean to null
    elif isinstance(value, list):
        return [corrupt_key_value(item) for item in value]
    elif isinstance(value, dict):
        return {k: corrupt_key_value(v) for k, v in value.items()}
    else:
        return value

def glitchy_json_parser(input_path, output_path):
    with open(input_path, 'r') as file:
        data = json.load(file)
    
    # Randomly select 10% of the key-value pairs to corrupt
    total_items = sum(len(v) if isinstance(v, dict) else 1 for v in data.values())
    items_to_corrupt = max(1, int(total_items * 0.1))
    flattened_data = []
    
    def flatten_json(y):
        out = {}
        
        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '_')
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
            else:
                out[name[:-1]] = x
        
        flatten(y)
        return out
    
    flattened_data = flatten_json(data)
    corrupted_items = random.sample(list(flattened_data.items()), items_to_corrupt)
    
    for key, _ in corrupted_items:
        flattened_data[key] = corrupt_key_value(flattened_data[key])
    
    def unflatten(dict_, sep='_'):
        result_dict = {}
        for key, value in dict_.items():
            parts = key.split(sep)
            d = result_dict
            for part in parts[:-1]:
                if part not in d:
                    d[part] = {}
                d = d[part]
            d[parts[-1]] = value
        return result_dict
    
    corrupted_data = unflatten(flattened_data)
    
    with open(output_path, 'w') as file:
        json.dump(corrupted_data, file, indent=4)

if __name__ == "__main__":
    input_json = "input.json"
    output_json = "corrupted_output.json"
    glitchy_json_parser(input_json, output_json)
```

This Python script reads a JSON file, randomly corrupts 10% of the key-value pairs by changing numbers to strings and booleans to null, and then writes the corrupted data to a new JSON file. The script includes functions to flatten and unflatten dictionaries to handle nested structures properly.