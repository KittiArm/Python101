# Assignment16

size = int(input("Enter size : "))
for row in range(size):
    for column in range(size):
        if row==0 or row==size-1 or column==0 or column==size-1:
            print("o", end="")
        else:
            print(" ", end="")
        
    print(" ")