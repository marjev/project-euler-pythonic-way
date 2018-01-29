import math


def get_fibonacci_numbers(limit):
    """ 
    Returns those Fibonacci numbers whose value does not exceed the limit.

    Args:
        limit (int): Upper limit which must not be exceeded.

    Yields:
        int: The next Fibonacci number in the range of 0 to `limit` - 1.
    """
    current, following = 0, 1

    while current < limit:
        yield current
        current, following = following, current + following


def get_nth_prime_number(n):
    """ 
    Returns the n-th prime number.

    Args:
        n (int): Index of the prime number.

    Returns:
        int: The n-th prime number.
    """
    if n == 1:
        return 2

    n -= 1
    prime_candidate = 1

    while n > 0:
        prime_candidate += 2
        if is_prime_number(prime_candidate):
            n -= 1
    return prime_candidate


def get_number_of_digits(number):
    """ 
    Returns the number of digits of a natural number.

    Args:
        number (int): Natural number whose number of digits is returned.

    Returns:
        int: Number of digits of a natural number.
    
    Raises:
        ValueError: If `number` is not a natural number.
    """
    if number < 1:
        raise ValueError('{number} is not a natural number.'.format(number=number))

    return len(str(number))


def greatest_common_divisor(a, b):
    """ 
    Returns the greatest common divisor (GCD) of two numbers.

    Args:
        a (int): First number for which the GCD is calculated.
        b (int): Second number for which the GCD is calculated.

    Returns:
        int: The GCD of two numbers
    """
    smaller_number, larger_number = (b, a) if a > b else (a, b)

    while smaller_number != 0:
        larger_number, smaller_number = smaller_number, larger_number % smaller_number

    return larger_number


def is_palindrome(text):
    """ 
    Returns whether the text is a palindrome.

    Args:
        text (str): String value that will be evaluated.

    Returns:
        bool: True if `text` is a palindrome. False otherwise.
    """
    return text == text[::-1]


def is_prime_number(number):
    """ 
    Returns whether the number is a prime number.

    Args:
        number (int): A number whose primality is tested.

    Returns:
        bool: True if `number` is the prime number. False otherwise.
    """
    if number < 2:
        return False

    if number % 2 == 0:
        return False

    square_root = math.sqrt(number)
    upper_limit = int(square_root)
    if square_root == upper_limit:
        return False

    for i in range(3, upper_limit + 1, 2):
        if number % i == 0:
            return False
    return True


def is_product_of_two_x_digit_numbers(number, number_of_digits):
    """ 
    Returns whether the number is a product of two numbers with the `number_of_digits` digits.

    Args:
        number (int): Natural number to be evaluated.
        number_of_digits (int): Number of digits used to evaluate a factor.

    Returns:
        bool: True if `number` is a product of two numbers with the `number_of_digits` digits. False otherwise.

    Raises:
        ValueError: If `number` is not a natural number.
        ValueError: If `number_of_digits` is not a natural number.
    """
    if number < 1:
        raise ValueError('{number} is not a natural number.'.format(number=number))

    if number_of_digits < 1:
        raise ValueError('Number of digits must be greater than zero.')

    square_root = int(math.sqrt(number))
    for i in range(square_root, smallest_natural_number(number_of_digits) - 1, -1):
        factor, remainder = divmod(number, i)
        if remainder == 0:
            number_of_factor_digits = get_number_of_digits(factor)
            if number_of_factor_digits == number_of_digits:
                return True
            elif number_of_factor_digits > number_of_digits:
                return False

    return False


def largest_natural_number(number_of_digits):
    """ 
    Returns the largest natural x-digit number.

    Args:
        number_of_digits (int): Number of digits of the largest number.

    Returns:
        int: The largest natural number that has `number_of_digits` digits.

    Raises:
        ValueError: If `number_of_digits` is not a natural number.
    """
    if number_of_digits < 1:
        raise ValueError('Number of digits must be greater than zero.')

    return 10 ** number_of_digits - 1


def largest_palindrome_product(number_of_digits):
    """ 
    Returns the largest palindrome number that is a product of two numbers with `number_of_digits` digits.

    Args:
        number_of_digits (int): Number of digits of the largest number.

    Returns:
        int: The largest palindrome product.
    
    Raises:
        ValueError: If `number_of_digits` is not a natural number.
    """
    if number_of_digits < 1:
        raise ValueError('Number of digits must be greater than zero.')

    max_possible_product = largest_natural_number(number_of_digits) ** 2

    for i in range(max_possible_product, 0, -1):
        if is_palindrome(str(i)) and is_product_of_two_x_digit_numbers(i, number_of_digits):
            return i


def largest_prime_factor(number):
    """ 
    Returns the largest prime factor of a natural number.

    Args:
        number (int): Natural number whose largest prime factor we're searching for.

    Returns:
        :obj:`int`: The largest prime factor or None if there's no such number.

    Raises:
        ValueError: If `number` is not a natural number.
    """
    if number < 1:
        raise ValueError('{number} is not a natural number.'.format(number=number))

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


def least_common_multiple(a, b):
    """ 
    Returns the least common multiple (LCM) of two numbers.

    Args:
        a (int): First number for which the LCM is calculated.
        b (int): Second number for which the LCM is calculated.

    Returns:
        int: The LCM of two numbers
    """
    return abs(a * b) // greatest_common_divisor(a, b)


def smallest_multiple_of_numbers(divisors):
    """ 
    Returns the smallest positive number that is evenly divisible by all provided numbers.

    Args:
        divisors (range): Divisors of the number.

    Returns:
        int: The smallest positive number that is evenly divisible by all provided numbers.
    """
    smallest_multiple = divisors[0]

    for i in range(1, len(divisors)):
        current_divisor = divisors[i]
        smallest_multiple = least_common_multiple(smallest_multiple, current_divisor)

    return smallest_multiple


def smallest_natural_number(number_of_digits):
    """ 
    Returns the smallest natural x-digit number.

    Args:
        number_of_digits (int): Number of digits of the smallest number.

    Returns:
        int: The smallest natural number that has `number_of_digits` digits.
    
    Raises:
        ValueError: If `number_of_digits` is not a natural number.
    """
    if number_of_digits < 1:
        raise ValueError('Number of digits must be greater than zero.')

    return 10 ** (number_of_digits - 1)


def sum_of_n_natural_numbers(n):
    """ 
    Returns the sum of the first n natural numbers.

    Args:
        n (int): number of natural numbers

    Returns:
        int: The sum of the first n natural numbers.
    """
    return n * (n + 1) // 2


def sum_of_squares_of_n_natural_numbers(n):
    """ 
    Returns the sum of the squares of the first n natural numbers.

    Args:
        n (int): number of natural numbers

    Returns:
        int: The sum of the squares of the first n natural numbers.
    """
    return n * (n + 1) * (2 * n + 1) // 6
