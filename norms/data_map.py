import json
import os
import re

class DataMap:
    def __init__(self, file_path):
        print("EEEEEEEEEEE",file_path)
        self.data_map = self.load_data_map(file_path)
    
    def load_data_map(self, file_path):
        with open(file_path, 'r') as f:
            data_map = json.load(f)
        return data_map
    
    def map_input_to_code(self, input_string):
        input_string = input_string.strip()  # Remove leading and trailing whitespace
        input_string = input_string.strip('()')
        
        print("Input:", input_string)
        
        if "|" in input_string:
            conditions = input_string.split(" | ")
            mapped_conditions = []
            for condition in conditions:
                if "&" in condition:
                    sub_conditions = condition.split(" & ")
                    mapped_sub_conditions = []
                    for sub_condition in sub_conditions:
                        mapped_sub_condition = self.map_single_condition(sub_condition)
                        if mapped_sub_condition:
                            mapped_sub_conditions.append(mapped_sub_condition)
                        else:
                            return "Invalid input format"
                    mapped_conditions.append(" & ".join(mapped_sub_conditions))
                else:
                    mapped_condition = self.map_single_condition(condition)
                    if mapped_condition:
                        mapped_conditions.append(mapped_condition)
                    else:
                        return "Invalid input format"
            return " | ".join(mapped_conditions)
        elif "&" in input_string:
            conditions = input_string.split(" & ")
            mapped_conditions = []
            for condition in conditions:
                mapped_condition = self.map_single_condition(condition)
                if mapped_condition:
                    mapped_conditions.append(mapped_condition)
                else:
                    return "Invalid input format"
            return " & ".join(mapped_conditions)
        else:
            return self.map_single_condition(input_string)

        
    def map_single_condition(self, condition):
        condition = condition.strip()  # Remove leading and trailing whitespace
        if "==" in condition:
            category, value = condition.split("==")
            category = category.strip()
            value = value.strip().strip("'")  # Remove leading and trailing single quotes

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
                    val = val.strip().strip("'")  # Remove leading and trailing single quotes
                    if val in self.data_map[category].values():
                        for key, map_val in self.data_map[category].items():
                            if map_val == val:
                                mapped_codes.append(key)
                    else:
                        return f"Value '{val}' not found in {category}"
                return f"{category} in {mapped_codes}"
            else:
                print("xxxx",condition)
                return condition
        else:
            return "Invalid input format"

    def format_condition(self, condition):
        if "['" in condition and "']" in condition:
            category, values = condition.split(" in ")
            values = values.replace("[", "").replace("]", "")  # Remove square brackets
            values = [int(val.strip().strip("'")) for val in values.split(",")]  # Convert values to integers
            formatted_condition = f"{category} in {values}"
        else:
            formatted_condition = condition  # No change needed
        return formatted_condition


    def format_input_string(self, input_string):
        # Split the input string based on dynamic logical operators ('&' and '|')
        conditions = re.split(r'\s([&|])\s', input_string)
        
        # Iterate over each condition and format it
        formatted_conditions = [self.format_condition(condition) for condition in conditions]
        
        # Join the formatted conditions back together using dynamic logical operators ('&' and '|')
        formatted_input_string = " ".join(formatted_conditions)
        
        return formatted_input_string

# file_path = os.path.join(os.getcwd(), "backend", "crosstab", "datamap.json")
# dm = DataMap(file_path)
# val = dm.map_input_to_code("secnew in ['SEC A', 'SEC B'] & projectname == 'Drumstick'")
# print(val)
# print(dm.format_input_string(val))
