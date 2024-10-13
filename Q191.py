# Write a Python program that prompts the user to enter numbers and stops only when the user enters “stop”. After this, 
# print the minimum even, maximum even, average of even number, minimum odd, maximum odd, average of odd   number 
# from among all the numbers entered by the user.
#  Note:   You are not allowed to use any built-in structures like lists, tuples, etc. or any built-in functions like max, min, sum

even_count = 0
even_sum = 0
min_even = None
max_even = None

odd_count = 0
odd_sum = 0
min_odd = None
max_odd = None

while True:
    user_input = input("Enter a number (or 'stop' to finish): ")
    
    if user_input.lower() == "stop":
        break
        
    num = int(user_input)
    
    if num % 2 == 0:
        even_count += 1
        even_sum += num
        
        if min_even is None or num < min_even:
            min_even = num
        if max_even is None or num > max_even:
            max_even = num
    else:
        odd_count += 1
        odd_sum += num
        
        if min_odd is None or num < min_odd:
            min_odd = num
        if max_odd is None or num > max_odd:
            max_odd = num

print(f"Minimum Even: {min_even}")
print(f"Maximum Even: {max_even}")
print(f"Average Even: {even_sum / even_count}")

print(f"Minimum Odd: {min_odd}")
print(f"Maximum Odd: {max_odd}")
print(f"Average Odd: {odd_sum / odd_count}")