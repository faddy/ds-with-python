def sequential_search(list_of_values, item):
    if not list_of_values or not item:
        return False

    pos = 0
    found = False

    while pos < len(list_of_values) and not found:
        if item == list_of_values[pos]:
            found = True
        pos += 1

    return found
