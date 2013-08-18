
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(values):
    '''
    bubble down the max value in the array to the end
    '''
    if not values or len(values) == 1:
        return

    n = len(values)

    for pass_num in range(n-1, 0, -1):
        for i in range(pass_num):
            if values[i+1] < values[i]:
                swap(values, i, i+1)


def selection_sort(values):
    """
    select the max value in the array and move it to the end
    """
    if not values or len(values) == 1:
        return

    n = len(values)

    for pass_num in range(n-1, 0, -1):
        max_val = values[0]
        max_index = 0

        for i in range(pass_num+1):
            if values[i] > max_val:
                max_val = values[i]
                max_index = i

        swap(values, max_index, pass_num)


def insertion_sort(values):
    """
    at pass i, list will be sorted up to ith element
    insert i+1th element into the sorted partial list
    """
    if not values or len(values) == 1:
        return

    n = len(values)

    for pass_num in range(1, n):
        temp = values[pass_num]
        i = pass_num

        while values[i-1] > temp and i != 0:
            values[i] = values[i-1]
            i -= 1

        values[i] = temp


def merge_sort(values):
    """
    merge_sort requires additional space to hold the two halves
    """
    if not values or len(values) == 1:
        return

    mid = len(values) / 2
    left_half = values[:mid]
    right_half = values[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    merge(values, left_half, right_half)


def merge(values, left_half, right_half):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            values[k] = left_half[i]
            i += 1
        else:
            values[k] = right_half[j]
            j += 1

        k += 1

    while i < len(left_half):
        values[k] = left_half[i]
        k += 1
        i += 1

    while j < len(right_half):
        values[k] = right_half[j]
        k += 1
        j += 1


#def merge_sort_indices(values, beg=None, end=None):
#    if not values:
#        return
#
#    if beg < end:
#        return
#
#    if beg is None or end is None:
#        beg = 0
#        end = len(values)-1
#
#    mid = (beg + end) / 2
#    merge_sort_indices(values, beg, mid)
#    merge_sort_indices(values, mid, end)


def quick_sort(values, beg=None, end=None):
    if not values or len(values) == 1:
        return

    if beg > end:
        return

    # for the first call
    if beg is None or end is None:
        beg = 0
        end = len(values)-1

    split_point = partition(values, beg, end)

    quick_sort(values, beg, split_point-1)
    quick_sort(values, split_point+1, end)


def partition(values, beg, end):
    pivot = values[beg]
    left  = beg + 1
    right = end
    done = False

    while not done:
        while left <= right and values[left] <= pivot:
            left += 1

        while left <= right and values[right] > pivot:
            right -= 1

        if left > right:
            done = True
        else:
            swap(values, left, right)

    swap(values, beg, right)

    return right



