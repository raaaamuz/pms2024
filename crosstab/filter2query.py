class FilterQueryClass:
    def filter_to_query(filter_string):
        # Split the filter string by "AND"
        conditions = filter_string.split(" AND ")

        # Initialize an empty list to store the query conditions
        query_conditions = []

        # Parse and construct query for each condition
        for condition in conditions:
            # Check if the condition contains "OR"
            if " OR " in condition:
                # If condition contains "OR", split and construct sub-queries
                sub_conditions = condition.split(" OR ")
                sub_query = " | ".join(parse_condition(sub_cond) for sub_cond in sub_conditions)
                query_conditions.append(f"({sub_query})")
            else:
                # Single condition without "OR"
                query_conditions.append(parse_condition(condition))

        # Join the query conditions with "AND" to construct the final query
        final_query = " & ".join(query_conditions)

        return final_query

    def parse_condition(condition):
        key, value = condition.split(":")
        key = key.strip()
        value = value.strip()

        # Check if value contains multiple options separated by comma
        if "," in value:
            options = [f"'{option.strip()}'" for option in value.split(",")]
            return f"{key} in [{', '.join(options)}]"
        else:
            return f"{key} == '{value}'"


    # Test the function
    #query_string = "jobno:MR3449 OR productcode:Egypt (E8G4) AND purchaseintentionpriced:Rating 1"
    #pandas_filter_query = filter_to_query(query_string)
    #print("Pandas Filter Query:")
    #print(pandas_filter_query)
