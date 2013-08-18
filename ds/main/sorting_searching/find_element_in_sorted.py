from utils import num_utils
import random


def make_array(N):
    arr = num_utils.generate_random_sorted_arr(N)
    num_utils.rotate(arr, random.randint(1, N))
    return arr


def find_item_in_array(arr, lower, upper, item):
    if not arr: return None

    while lower <= upper:
        print 'searching:', arr[lower:upper]
        mid = (lower + upper)/2

        if arr[mid] == item:
            return mid

        elif arr[lower] < arr[mid]:
            # left half of array is monotonously increasing
            # => starting point is in the right sub array
            if item > arr[mid]:
                lower = mid + 1		# item is in left subarray
            elif item >= arr[lower]:
                upper = mid - 1		# item is in right subarray
            else:
                lower = mid + 1

        else:
            # arr[lower] is greater than arr[mid]
            # starting point is in the left subarray
            if item < arr[mid]:
                upper = mid - 1
            elif item <= arr[upper]:
                lower = mid + 1
            else:
                upper = mid - 1


if __name__ == '__main__':
    n = 20
    a = make_array(n)
    print find_item_in_array(a, 0, len(a) - 1, 16)
