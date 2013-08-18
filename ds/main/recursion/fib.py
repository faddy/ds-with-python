
def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    return fib(n-1) + fib(n-2)


## Using memoization
cache = {}
def fib_memo(n):
    if n == 0: return 0
    if n == 1: return 1

    val = cache.get(n, None)
    if not val:
        val = fib_memo(n-1) + fib_memo(n-2)
        cache[n] = val

    return val


## Using memoization but with caching done in a decorator
## Notice how there is no caching logic in the actual code of fib_dec
new_cache = {}

def check_cache(f):
    def wrapper(n):
        val = new_cache.get(n, None)
        if not val:
            val = f(n)
            new_cache[n] = val
        return val

    return wrapper

@check_cache
def fib_dec(n):
    if n == 0: return 0
    if n == 1: return 1

    return fib_dec(n-1) + fib_memo(n-2)
