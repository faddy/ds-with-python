def swap(arr, i, j):
    print 'swapping:', i, j
    arr[i], arr[j] = arr[j], arr[i]


def sort_list(values):
    if not values or len(values) == 1: return values

    start = 0
    end = len(values) - 1
    i = 0

    while i < end:
        print values
        if values[i] == 3:
            swap(values, i, end)
            end -= 1

        elif values[i] == 1:
            swap(values, i, start)
            start += 1

        else:
            i += 1



