def product_of_string_digits(string):
    """
    Returns the product of the digits.

    Args:
        number (str): number in the string format whose digits are multiplied to form a product.

    Returns:
        int: The product of the digits of the stringified number.
    """
    if '0' in string:
        return 0

    product = 1

    for character in string:
        digit = int(character)
        product *= digit

    return product
