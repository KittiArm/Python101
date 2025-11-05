# Assignment11

sum = 0
while sum < 100: # stop cause wihle condition
    number = int(input("Enter number : "))
    sum+=number
print(f"Summation = {sum}")

sum = 0
while True:
    number = int(input("Enter number : "))
    sum+=number
    if sum>=100: # stop casue condition in while
        break 
print(f"Summation = {sum}")