# Gross Pay, Annual Income and Income Tax Calculator
# Write a Python Program to make the gross pay, annual income and income tax calculator using following data.
# The gross pay consists of Basic Pay, House Rent Allowance (hra), Dearness Allowance (dra), other allowances and professional tax and provident fund.
# Gross Pay= Basic Pay+ House Rent Allowance (hra) + Dearness Allowance (dra) +other allowances +Transport Allowance(TA)– Professional tax –Employees’ Provident fund (EPF)
# Basic Pay for different grade levels are indicated in table given.
# The Professional tax remains constant and that is equal to 200 Rs. for each grade levels and each month.
# House Rent Allowance (hra) varies as per the city- For Class 1 Cities it is 0.3 times of Basic Pay of each grade levels, for Class 2 Cities it is 0.2 times of Basic Pay of each grade levels, for Class 3 Cities it is 0.
# 1 times of Basic Pay of each grade levels,Dearness Allowance (dra)= 0.5 times of Basic Pay of each grade levels, Other allowances are given in table which varies according to different grade levels, Provident Fund= 0.11 times of Basic Pay for each grade levels, Transport Allowance remains constant as 900 Rs. for each levels.
# For different grade pays:
# The gross pay calculated is only for one month.
# After calculating Gross Pay of each employee calculate the annual pay for employee by multiplying gross pay calculated, by 12.
# So, Annual Pay of an employee=Gross Pay of an employee*12

professional_tax = 200
hra = None
dra = 0.5
epf = 0.11
ta = 900
gl = None
oa = None

grade_level = [['A',60000,800],['B',50000,7000],['C',40000,6000],['D',30000,5000],['E',20000,4000],['F',10000,3000]]

x = input('Enter the grade_level (A,B,C,D,E or F) : ')
for i in range(len(grade_level)):
    if x == grade_level[i][0]:
        gl = grade_level[i][1]
        oa = grade_level[i][2]
        break

if gl == None:
    print('Select valid level')
else: 
    print('city 1 is a tier 1 (metro), city 2 is tier 2, and city 3 is tier 3')
    x = input('Enter the city (1,2 or 3) : ')
    x = int(x)

    if x == 1 or x == 2 or x == 3:
        hra = 0.3 if x == 1 else (0.2 if x == 2 else 0.1)
        
    gross_pay = gl + gl * hra + gl * dra + oa + ta - professional_tax - gl * epf
    annual_pay = gross_pay * 12
    
    income_tax = 0
    if annual_pay <= 250000:
        income_tax = 0
    elif annual_pay <= 500000:
        income_tax = (annual_pay - 250000) * 0.05
    elif annual_pay <= 750000:
        income_tax = (annual_pay - 500000) * 0.1 + 12500
    elif annual_pay <= 1000000:
        income_tax = (annual_pay - 750000) * 0.15 + 37500
    elif annual_pay <= 1250000:
        income_tax = (annual_pay - 1000000) * 0.2 + 75000
    elif annual_pay <= 1500000:
        income_tax = (annual_pay - 1250000) * 0.25 + 125000
    else:
        income_tax = (annual_pay - 1500000) * 0.3 + 187000

    print(f'Gross Pay: Rs.{gross_pay}')
    print(f'Annual Pay: Rs.{annual_pay}')
    print(f'Income Tax: Rs.{income_tax}')
