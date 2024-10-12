# Draw a pattern using a python program:
#  1
#  0  1
#  1  0  1
#  0  1  0  1
for i in range (1,5):
    for j in range (1, i+1):
        print(int((i+j) % 2 == 0),' ',end="")
    print()