import random


def generate_random_sorted_arr(n):
    diff_range = 10
    arr = []
    num = 5
    for i in range(n):
        arr.append(num)
        num += random.randint(1, diff_range)
    return arr


def rotate(arr, count):
    for c in range(count):
        temp = arr[0]
        for i in range(len(arr) - 1):
            arr[i] = arr[i+1]
        arr[i+1] = temp


