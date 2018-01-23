import math


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


def get_largest_natural_number(number_of_digits):
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


def get_largest_palindrome_product(limit, number_of_digits):
    """ 
    Returns the largest palindrome number:
        - whose value does not exceed the limit
        - is a product of two numbers with `number_of_digits` digits

    Args:
        limit (int): Upper limit which must not be exceeded.
        number_of_digits (int): Number of digits of the largest number.

    Returns:
        int: The largest palindrome number in the range of 0 to `limit`.
    
    Raises:
        ValueError: If `number_of_digits` is not a natural number.
    """
    if number_of_digits < 1:
        raise ValueError('Number of digits must be greater than zero.')

    for i in range(limit, 0, -1):
        if is_palindrome(str(i)) and is_product_of_two_x_digit_numbers(i, number_of_digits):
            return i


def get_largest_prime_factor(number):
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
        raise ValueError('%d is not a natural number.' % number)

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


def get_lowest_natural_number(number_of_digits):
    """ 
    Returns the lowest natural x-digit number.

    Args:
        number_of_digits (int): Number of digits of the lowest number.

    Returns:
        int: The lowest natural number that has `number_of_digits` digits.
    
    Raises:
        ValueError: If `number_of_digits` is not a natural number.
    """
    if number_of_digits < 1:
        raise ValueError('Number of digits must be greater than zero.')

    return 10 ** (number_of_digits - 1)


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
        raise ValueError('%d is not a natural number.' % number)

    return len(str(number))


def is_palindrome(text):
    """ 
    Returns whether the text is a palindrome.

    Args:
        text (str): String value that will be evaluated.

    Returns:
        bool: True if `text` is a palindrome. False otherwise.
    """
    return text == text[::-1]


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
        raise ValueError('%d is not a natural number.' % number)

    if number_of_digits < 1:
        raise ValueError('Number of digits must be greater than zero.')

    square_root = int(math.sqrt(number))
    for i in range(square_root, get_lowest_natural_number(number_of_digits) - 1, -1):
        factor, remainder = divmod(number, i)
        if remainder == 0:
            if is_x_digit_natural_number(factor, number_of_digits):
                return True
            elif get_number_of_digits(factor) > number_of_digits:
                return False

    return False


def is_x_digit_natural_number(number, number_of_digits):
    """ 
    Returns whether the natural number has `number_of_digits` digits.

    Args:
        number (int): Natural number to be evaluated.
        number_of_digits (int): Number of digits used to evaluate a number.

    Returns:
        bool: True if `number` has `number_of_digits` digits. False otherwise.

    Raises:
        ValueError: If `number` is not a natural number.
    """
    if number < 1:
        raise ValueError('%d is not a natural number.' % number)

    return get_lowest_natural_number(number_of_digits) <= number <= get_largest_natural_number(number_of_digits)
