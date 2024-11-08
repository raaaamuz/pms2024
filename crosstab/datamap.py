import json
import os

def convert_keys_to_int(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    updated_data = {}
    for key, value in data.items():
        try:
            updated_key = int(key)
            updated_data[updated_key] = value
        except ValueError:
            # Skip keys that cannot be converted to integers
            pass

    with open(output_file, 'w') as file:
        json.dump(updated_data, file, indent=4)

current_folder_path = os.getcwd()
print("Current folder path:", current_folder_path)

# Input and output file paths
input_file = os.path.join(current_folder_path, "backend", "crosstab", "datamap.json")
output_file = os.path.join(current_folder_path, "backend", "crosstab", "datamap_formatted.json")

# Call the function
convert_keys_to_int(input_file, output_file)

print("Conversion complete. Output saved to output.json")
