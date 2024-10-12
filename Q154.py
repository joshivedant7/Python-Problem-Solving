#  Write a program to find the maximum number among the three input numbers.
num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))
num_3 = int(input("Enter number 3: "))
print('Max is :' , num_1 if num_1 >= num_2 and num_1 >= num_3 else (num_2 if num_2 >= num_1 and num_2 >= num_3 else num_3))
