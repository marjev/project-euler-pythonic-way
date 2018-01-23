from extended_math import get_largest_natural_number, get_largest_palindrome_product


number_of_digits = 2
largest_three_digited_number = get_largest_natural_number(number_of_digits)
max_possible_product = largest_three_digited_number ** 2

largest_palindrome = get_largest_palindrome_product(max_possible_product, number_of_digits)
print(largest_palindrome)
