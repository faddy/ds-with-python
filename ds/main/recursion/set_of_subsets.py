# [1, 2, 3] --> [ [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3] ]
# [1, 2]
# [1] -> [[1] + f([])] = [ [1] + x for x in [[]] ] = 


def set_of_subsets(values_list):

    if not values_list:
        return [[]]

    curr_val = values_list[0]
    subsets_of_other_vals = set_of_subsets(values_list[1:])

    new_set = subsets_of_other_vals + [[curr_val] + s for s in subsets_of_other_vals]
    return new_set


