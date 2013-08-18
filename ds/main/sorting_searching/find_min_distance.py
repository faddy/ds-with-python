
def find_min_distance(arr1, arr2):
    if arr1[-1] < arr2[0]:
        return (arr1[-1], arr2[0])

    if arr2[-1] < arr1[0]:
        return (arr2[-1], arr1[0])

    while True:
        
