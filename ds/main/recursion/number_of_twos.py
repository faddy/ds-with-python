
def count_digits(n):
    count = 0
    while n > 0:
        n = n / 10
        count += 1

    return count


def get_step(n):
    n -= 1
    no_of_digits = count_digits(n)
    return 10 ** (no_of_digits - 1)


def first_digit(n):
    return int(str(n)[0])



cache = {}

def get_two_count(n):
    if n < 2:
        return 0

    if 2 <= n <= 10:
        return 1

    if n in cache: return cache[n]

    step = get_step(n)
    total = 0

    for i in range(0, n, step):
        nxt = min(i+step, n)
        if first_digit(i) == 2:
            total += (nxt - i)

        total += get_two_count(nxt - i)

    cache[n] = total
    return total
