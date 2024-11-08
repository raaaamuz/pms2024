import json
import os
import re

class DataMap:
    def __init__(self, file_path):
        self.data_map = self.load_data_map(file_path)
    
    def load_data_map(self, file_path):
        with open(file_path, 'r') as f:
            data_map = json.load(f)
        return data_map
    
    def map_input_to_code(self, input_string):
        input_string = input_string.strip().strip('()')
        print("Input:", input_string)
        
        # Handling logical OR and AND operations
        if "|" in input_string:
            return self.map_complex_condition(input_string, " | ")
        elif "&" in input_string:
            return self.map_complex_condition(input_string, " & ")
        else:
            return self.map_single_condition(input_string)

    def map_complex_condition(self, input_string, delimiter):
        conditions = input_string.split(delimiter)
        mapped_conditions = [self.map_single_condition(condition) for condition in conditions]
        if any(c.startswith("Invalid") for c in mapped_conditions):
            return "Invalid input format"
        return delimiter.join(mapped_conditions)

    def map_single_condition(self, condition):
        condition = condition.strip()
        if "==" in condition:
            category, value = map(str.strip, condition.split("=="))
            value = value.strip("'")
            return self.map_value(category, value, equality=True)
        elif " in " in condition:
            category, values = map(str.strip, condition.split(" in "))
            values = eval(values)  # This could be a security risk with eval. Consider alternatives.
            if not isinstance(values, list):
                return "Invalid input format"
            mapped_values = [self.map_value(category, val.strip("'"), equality=False) for val in values]
            if any("Invalid" in val for val in mapped_values):
                return "Invalid input format"
            return f"{category} in [{', '.join(mapped_values)}]"
        else:
            return "Invalid input format"

    def map_value(self, category, value, equality):
        if category in self.data_map:
            # Look for the value directly
            for key, val in self.data_map[category].items():
                if value.lower() == val.lower():  # Case insensitive comparison
                    mapped_value = key
                    break
            else:
                # Value not found after checking all entries
                return f"Value '{value}' not found in {category}"

            if equality:
                return f"{category}=={mapped_value}"
            else:
                return str(mapped_value)

        else:
            # Handle years as special case
            if category == "year" and value.isdigit():
                return f"{category}=={int(value)}" if equality else str(int(value))

            # If it's not a known category and not a year, handle accordingly
            if value.isdigit():
                return f"{category}=={int(value)}" if equality else str(int(value))
            else:
                return f"{category}=='{value}'" if equality else f"'{value}'"


# #Assuming a certain file_path, not directly executable without the file
# file_path = os.path.join(os.getcwd(), "backend", "crosstab", "datamap.json")
# dm = DataMap(file_path)
# #example_input = "blindbranded == 'Blind' & year in ['2019','2022'] & clientname in ['Nadec', 'KELLOGG MARKETING AND SALES COMPANY (UK)']"
# #example_input="blindbranded=='Blind' & year == 2019 & clientname in ['Nadec', 'KELLOGG MARKETING AND SALES COMPANY (UK)']"
# example_input="secnew in ['SEC A', 'SEC B']"
# print(dm.map_input_to_code(example_input))
