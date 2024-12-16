import json

# Function to read facet keys from a text file
def read_facet_keys(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

# Function to find keys in A that are not in B
def find_mismatched_keys(a, b):
    mismatches = {}

    for key_a in a:
        found_match = False
        for key_b in b:
            # Check for a match by stripping special characters and comparing
            if key_a.replace("_", "").lower() == key_b.replace("attributes.", "").replace("_", "").lower():
                found_match = True
                break
        
        if not found_match:
            mismatches[key_a] = "No match in B"  # Key in A but not in B

    return mismatches

# Paths to the input text files
file_a = './searchspring_facets.txt'
file_b = './vertexai_facets.txt'
output_file = 'mismatched_keys.json'  # Output file path

# Read the facet keys from the files
search_engine_a = read_facet_keys(file_a)
search_engine_b = read_facet_keys(file_b)

# Get the mismatched keys
mismatched_keys = find_mismatched_keys(search_engine_a, search_engine_b)

# Write the results to a JSON file
with open(output_file, 'w') as outfile:
    json.dump(mismatched_keys, outfile, indent=4)

print(f'Mismatched keys saved to {output_file}')