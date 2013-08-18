
def get_k_largest(arr, k, beg=None, end=None):
    if not arr or len(arr) == 1: return

    if beg > end:
        beg = 0
        end = len(arr) - 1

    pivot = partition(arr, beg, end)

    if k < pivot:
