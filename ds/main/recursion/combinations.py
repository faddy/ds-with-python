
def get_combinations(values):
    """
    input : [ [1,4,3], [2,5], [6,7,9]]
    output: [ [1,2,6], [1,2,7], [1,2,9], [1,5,6],... ]
    """
    if not values: return []

    if len(values) == 1:
        return [[x] for x in values[0]]

    item = values[0]
    sub_combinations = get_combinations(values[1:])
    combinations = []

    for i in item:
        combination = [ [i] + sub_combination for sub_combination in sub_combinations]
        combinations.extend(combination)

    return combinations
