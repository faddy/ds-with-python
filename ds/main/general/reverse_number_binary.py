
def get_number_of_bits(n):
    if n == 0: return 1

    count = 0
    while n > 0:
        n /= 2
        count += 1

    return count


def reverse_number_binary(n):

    bit_count = get_number_of_bits(n)
    print 'bit_count = ', bit_count
    count = 0
    total = 0

    while n > 0:
        bit_value = n % 2
        total += bit_value * 2**(bit_count - count - 1)
        count += 1
        n /= 2

    return total
