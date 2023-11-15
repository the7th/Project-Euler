# This is for problem 4 of ProjectEuler https://projecteuler.net/problem=4

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product(n_digits):
    max_num = 10**n_digits - 1  # Largest n-digit number
    min_num = 10**(n_digits - 1)  # Smallest n-digit number
    max_palindrome = 0
    factors = (0, 0)

    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            product = i * j
            if product <= max_palindrome:
                break  # Further products will be smaller
            if is_palindrome(product):
                max_palindrome = product
                factors = (i, j)

    return max_palindrome, factors

print (largest_palindrome_product(3))

