# Assignment13
# Ladder number

'''
1
12
123
1234
12345
123456
'''

last = int(input("Enter number : "))
for row in range (1, last+1):
    for column in range(1, row+1):
        print(column, end='')
    print(" ")