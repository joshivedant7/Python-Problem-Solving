# Write a python program to swap first and last digits of a number.
x = int(input('Enter number : '))

def swap_first_last_digits(num):
    num_str = str(num) 
    if len(num_str) == 1:
        return num

    first_digit = num_str[0]
    last_digit = num_str[-1]

    swapped_num_str = last_digit + num_str[1:-1] + first_digit

    return int(swapped_num_str)

swapped_num = swap_first_last_digits(x)
print("Swapped number :", swapped_num)