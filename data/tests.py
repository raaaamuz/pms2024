import re

class DataProcessor:
    def remove_delimited_substrings(self, input_string):
        print("Input:", input_string)
        # Define the regex pattern to match text between " |()| " including the delimiters
        pattern = r'\s*\|\(\s*\d+\s*\)\|\s*'
        # Use re.sub to replace the matching patterns with an empty string
        result = re.sub(pattern, '', input_string)
        print("Output:", result)
        return result

# Example usage
processor = DataProcessor()
input_string = "xxxxxxxxxxpppppppppp clientname: KELLOGG MARKETING AND SALES COMPANY (UK) |( 636 )|\nyyyypppppppppppp clientname: KELLOGG MARKETING AND SALES COMPANY (UK) |( 636 )|"
output_string = processor.remove_delimited_substrings(input_string)
print(output_string)
