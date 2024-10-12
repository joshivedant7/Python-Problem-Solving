# Write a program to find the factorial of a number provided by the user.
a = int(input('Enter num : '))
factorial = 1
for i in range(1,a +1):
    factorial*=i
print(f"Factorial of {a} is {factorial}")