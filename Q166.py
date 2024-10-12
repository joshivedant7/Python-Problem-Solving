# Write a program to check if a number is prime or not.
n = int(input("Enter number : "))
m = int(n**0.5) + 1
for i in range(2,m):
    if n % i == 0:
        print("Ain't prime number")
        break
else : print("Prime number")