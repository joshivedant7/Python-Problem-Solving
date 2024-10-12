#  Write a Python program to print the multiplication table of given number by user
a = int(input('Enter num : '))
for i in range(1,11) :
    print(f"{a} x {i} = {a*i}")