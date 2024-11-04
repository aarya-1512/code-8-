def convert_to_dictionary(data_list):
    result_dict = {}
    
    # Iterate through each tuple in the list
    for key, value in data_list:
        # Assign the first element as key and the second element as value in the dictionary
        result_dict[key] = value
        
    return result_dict

# Given list of tuples
data_list = [('apple', 5), ('banana', 2), ('orange', 8), ('grapes', 3), ('pineapple', 1)]

# Call the function and store the resulting dictionary
converted_dict = convert_to_dictionary(data_list)

# Display the original list and the converted dictionary
print("Original List of Tuples:", data_list)
print("Converted Dictionary:", converted_dict)
