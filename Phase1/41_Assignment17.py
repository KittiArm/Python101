# Assignment17
# Add dice (1 - 6)

import random

_random = random.randrange(1, 7)
k = 1

while True:
    number = int(input("Guess number : "))
    correct = (number==_random)
    if number<0 or k==3:
        break
    if correct:
        print("Great!!!!!")
    else:
        if number>_random:
            print("Your number is more than the correct answer.")
        if number<_random:
            print("Your number is less than the correct answer.")
        print("Try again")
    k+=1
print(f"Answer is {_random}")