def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
