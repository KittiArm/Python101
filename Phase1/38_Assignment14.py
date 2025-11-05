# Assignment13
# Make a square

'''
3x3
xxx
xxx
xxx

5x5
xxxxx
xxxxx
xxxxx
xxxxx
xxxxx
'''

size = int(input("Enter size : "))

for row in range(size):
    for column in range(size):
        print("x", end="")
    print(" ")