# Write a program to print prime numbers between given interval from user
z = int(input("Enter number : "))
for i in range(2, z+1):
    n = i
    m = int(n**0.5) + 1
    for i in range(2,m):
        if n % i == 0:
            break
    else : print(f"{n}, ",end="")