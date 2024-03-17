def count_occurrences(elements):  
    occurrence_dict = {}
    for element in elements:
        if element in occurrence_dict:
            occurrence_dict[element] += 1
        else:
            occurrence_dict[element] = 1
    return occurrence_dict

elements_list = [1, 2, 3, 2, 1, 4, 5, 2, 3, 4, 1]
result = count_occurrences(elements_list)
print(result)
