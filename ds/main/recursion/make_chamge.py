denoms = [1, 5, 10, 25]


def make_change(n):
    if n <= 0: return 0

    return _make_change(n, 3)


def _make_change(n, index):

    if index == 0: return 1

    denom = denoms[index]

    ways = 0
    multiplier = 0

    while denom * multiplier <= n:
        ways += _make_change(n - denom * multiplier, index-1)
        multiplier += 1

    return ways
