
def remove_neighbors(i, possible_values):
    ind = possible_values.index(i)
    left_index = max(0, ind-1)
    right, left = possible_values[:left_index], possible_values[ind+2:]
    return right + left


def sum_no_neighbors(possible_values):
    if not possible_values:
        return 0

    if len(possible_values) == 1: return possible_values[0]

    if len(possible_values) == 2: return max(possible_values)

    max_val = 0
    for i in possible_values:
        new_possible_values = remove_neighbors(i, possible_values)

        val = i + sum_no_neighbors(new_possible_values)
        if val > max_val:
            max_val = val

    return max_val

