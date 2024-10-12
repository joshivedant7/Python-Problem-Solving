# Write a program to check if year is a leap year or not
year = int(input('Enter year : '))
if year % 400 == 0 or ( year % 100 != 0 and year % 4 ==0) :
    print(year,'is leap year')
else : print("Ain't leap year")