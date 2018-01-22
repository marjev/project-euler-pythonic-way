def get_fibonacci_numbers(limit):
    """ 
    Return those Fibonacci numbers whose value does not exceed the limit.

    Args:
        limit (int): Upper limit which must not be exceeded.

    Yields:
        int: The next Fibonacci number in the range of 0 to `limit` - 1.
    """
    current, following = 0, 1

    while current < limit:
        yield current
        current, following = following, current + following


suma = sum(i for i in get_fibonacci_numbers(4000000) if i % 2 == 0)

print(suma)
