def map_input_to_code(input_string):
    # Define the mappings
    mappings = {
        "blindbranded": {
            "Blind": "1",
            "Branded": "2"
        },
        "secnew": {
            "SEC A": "1",
            "SEC B": "2",
            "SEC C1": "3",
            "SEC C2": "4",
            "SEC D": "5",
            "SEC E": "6"
        },
        "studytype" : {
            "1":"Concept test",
            "2":"Product test",
            "3":"Concept Product test",
            "4":"Pack test",
            "5":"Ad test",
            "6":"Concept Pack test",
            "7":"Product Pack test",
            "8":"Concept Product Pack test"

        },
        # Add more mappings for other categories if needed
    }

    # Check if input contains "in"
    if "in" in input_string:
        split_input = input_string.split(" in ")
        category = split_input[0].strip()
        values = eval(split_input[1].strip())  # Safely evaluate the list of values
        
        # Check if the category exists in mappings
        if category in mappings:
            mapped_codes = []
            # Loop through the input values
            for value in values:
                # Check if the value exists in the category mappings
                if value in mappings[category]:
                    # Append the mapped code to the list
                    mapped_codes.append(mappings[category][value])
                else:
                    return f"Value '{value}' not found in {category}"
            # Return the formatted string with mapped codes
            return f"{category} in {mapped_codes}"
        else:
            return f"Category '{category}' not found in mappings"
    elif ":" in input_string:
        split_input = input_string.split(":")
        category = split_input[0].strip()
        value = split_input[1].strip()
        
        # Check if the category exists in mappings
        if category in mappings:
            # Check if the value exists in the category mappings
            if value in mappings[category]:
                # Return the formatted string with mapped code
                return f"{category}=={mappings[category][value]}"
            else:
                return f"Value '{value}' not found in {category}"
        else:
            return f"Category '{category}' not found in mappings"
    else:
        return "Invalid input format"

# Example usage:
print(map_input_to_code("secnew in ['SEC A', 'SEC B', 'SEC C1']"))  # Output: secnew in [1, 2, 3]
print(map_input_to_code("studytype:Concept Product test"))  # Output: secnew==1
