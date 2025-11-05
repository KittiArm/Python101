# Assignment19

number = []
while True:
    x = int(input("Enter your single number : "))
    if x < 0 :
        break
    number.append(x)

print(f"Before : {number}")
print(f"Min number : {min(number)}")
print(f"Max number : {max(number)}")
print(f"Summation : {sum(number)}")
