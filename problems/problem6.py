from extended_math import sum_of_n_natural_numbers, sum_of_squares_of_n_natural_numbers


n = 100
difference_between_two_sums = sum_of_n_natural_numbers(n) ** 2 - sum_of_squares_of_n_natural_numbers(n)

print(difference_between_two_sums)
