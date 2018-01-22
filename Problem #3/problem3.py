def get_largest_prime_factor(number):
    """ 
    Returns the largest prime factor of the number.

    Args:
        number (int): Number whose largest prime factor we're searching for.

    Returns:
        :obj:`int`: The largest prime factor or None if there's no such number.
    """
    divisor = 2
    largest_prime_factor = number

    while divisor < largest_prime_factor:
        if largest_prime_factor % divisor == 0:
            largest_prime_factor //= divisor
        else:
            divisor += 1

    if largest_prime_factor == number:
        return None

    return largest_prime_factor


largest_prime_factor = get_largest_prime_factor(600851475143)
print(largest_prime_factor)
