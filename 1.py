def unique_elements(input_list):

    unique_set = set(input_list)

    unique_list = list(unique_set)
    return unique_list


input_list = [1, 2, 3, 4, 2, 3, 5]
print(unique_elements(input_list))
