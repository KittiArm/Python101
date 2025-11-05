# Assignment15
# Make Checkers table

'''
x = Brown
o = White
'''

size = int(input("Enter size : "))

for row in range(size):
    for column in range(size):
        if (row+column)%2 == 0:
            print("x", end="")
        else:
            print("o", end="")
    print(" ")