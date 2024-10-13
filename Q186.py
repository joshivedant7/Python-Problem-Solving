# Write a program to implement the calculator for the date of Easter.
#  The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.
#  Ask the user to enter a year. Compute the following:
#  1.a = year % 19
#  2.b = year % 4
#  3.c = year % 7
#  4.d = (19 * a + 24) % 30
#  5.e = (2 * b + 4 * c + 6 * d + 5) % 7
#  6.dateofeaster = 22 + d + e
#  Special note: The algorithm can give a date in April. You will know that the date is in April if the calculation gives you an 
# answer greater than 31. (You’ll need to adjust) Also, if the year is one of four special years (1954, 1981, 2049, or 2076) 
# then subtract 7 from the date.

year = int(input("Enter a year between 1900 and 2099: "))

a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
date_of_easter = 22 + d + e

if date_of_easter > 31:
        day = date_of_easter - 31
        month = "April"
else:
    day = date_of_easter
    month = "March"

if year in [1954, 1981, 2049, 2076]:
    day -= 7
    if day <= 0:
        month = "March"
        day += 31

print(f'Easter day : {day}-{month}-{year}')