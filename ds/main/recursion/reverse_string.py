
def reverse_using_recursion(s):

    if not s: return ''

    if len(s) <= 1: return s

    return s[-1] + reverse_using_recursion(s[1:-1]) + s[0]



def reverse_using_iteration(s):

    if not s: return ''

    if len(s) <= 1: return s

    arr = list(s)
    l = len(arr)
    for i in range(l/2):
        swap(arr, i, l-1-i)

    return ''.join(arr)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

