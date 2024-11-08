import json
import os

class DataMap:
    def __init__(self, file_path):
        self.data_map = self.load_data_map(file_path)
    
    def load_data_map(self, file_path):
        with open(file_path, 'r') as f:
            data_map = json.load(f)
        return data_map
    
    def map_input_to_code(self, input_string):
        input_string = input_string.strip()  # Remove leading and trailing whitespace
        input_string = input_string.strip("()")  # Remove parentheses if present
        print("Input:", input_string)
        
        if "|" in input_string:
            conditions = input_string.split(" | ")
            mapped_conditions = []
            for condition in conditions:
                mapped_condition = self.map_single_condition(condition)
                if mapped_condition:
                    mapped_conditions.append(mapped_condition)
                else:
                    return "Invalid input format"
            return " | ".join(mapped_conditions)
        else:
            return self.map_single_condition(input_string)
        
    def map_single_condition(self, condition):
        condition = condition.strip()  # Remove leading and trailing whitespace
        if "==" in condition:
            category, value = condition.split("==")
            category = category.strip()
            value = value.strip()

            if category in self.data_map:
                if value in self.data_map[category].values():
                    for key, val in self.data_map[category].items():
                        if val == value:
                            return f"{category}=={key}"
                else:
                    return f"Value '{value}' not found in {category}"
            else:
                return condition
        elif "in" in condition:
            category, value = condition.split(" in ")
            category = category.strip()
            values = eval(value.strip())  # Safely evaluate the list of values

            if category in self.data_map:
                mapped_codes = []
                for val in values:
                    if val in self.data_map[category].values():
                        for key, map_val in self.data_map[category].items():
                            if map_val == val:
                                mapped_codes.append(key)
                    else:
                        return f"Value '{val}' not found in {category}"
                return f"{category} in {mapped_codes}"
            else:
                return condition
        else:
            return "Invalid input format"

# Usage example:
file_path = os.path.join(os.getcwd(), "backend", "crosstab", "datamap.json")
dmap = DataMap(file_path)

# Test cases
test_strings = [
    "secnew == 'SEC A'",
    "secnew in ['SEC A', 'SEC B', 'SEC C1']",
    "secnew in ['SEC A', 'SEC B', 'SEC C1'] | overallopinion in ['Rating 4', 'Rating 3']"
]

for test_str in test_strings:
    print("Result:", dmap.map_input_to_code("secnew == 'SEC A'"))
