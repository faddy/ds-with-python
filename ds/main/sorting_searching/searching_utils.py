
def binary_search(list_of_values, item):
    if not list_of_values or item is None:
        return False

    lower = 0
    upper = len(list_of_values) - 1
    found = False

    while lower <= upper and not found:
        mid   = (lower + upper) / 2

        if list_of_values[mid] == item:
            found = True

        elif item < list_of_values[mid]:
            upper = mid - 1

        else:
            lower = mid + 1

    return found


def binary_search_recursive(list_of_values, item):

    if not list_of_values or item is None:
        return False

    mid = (0 + len(list_of_values) - 1)/2

    if list_of_values[mid] == item:
        return True

    elif item < list_of_values[mid]:
        return search_recursive(list_of_values[:mid], item)

    else:
        return search_recursive(list_of_values[mid+1:], item)


def binary_search_recursive_with_indices(values, start, end, item):
    if not values or item is None:
        return False

    if not start < end:
        return False

    mid = (start + end) / 2
    if values[mid] == item:
        return True

    elif item < values[mid]:
        return search_rec_with_indices(values, start, mid - 1, item)

    else:
        return search_rec_with_indices(values, mid + 1, end, item)


