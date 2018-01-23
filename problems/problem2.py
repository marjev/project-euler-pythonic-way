from extended_math import get_fibonacci_numbers


suma = sum(i for i in get_fibonacci_numbers(4000000) if i % 2 == 0)

print(suma)
