
def merge_sort(arr):
    if not arr: return None
    if len(arr) == 1: return arr

    mid = len(arr) / 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(p, q):
    new = []
    i = j = 0

    while i < len(p) and j < len(q):
        if p[i] < q[j]:
            new.append(p[i])
            i += 1
        else:
            new.append(q[j])
            j += 1

    while i < len(p):
        new.append(p[i])
        i += 1

    while j < len(q):
        new.append(q[j])
        j += 1

    return new


def quicksort(arr):
    pass

def test():
    arr1 = [5, 3, 9, 19, 2, 3, 1, 4]
    arr2 = [2]

    print merge_sort(arr1)
