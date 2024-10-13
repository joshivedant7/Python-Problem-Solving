#  Write a program that enters a single digit integer number and produces all possible 6-digit numbers for which the product  of their digits is equal to the entered number.

def product_of_digits(n):
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product

n = int(input("Enter a single digit integer (0-9): "))
for i in range(100000, 1000000):
    if product_of_digits(i) == n:
        print(i)