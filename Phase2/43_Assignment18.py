# Assignment18

number = []
while True:
    x = int(input("Enter your single number : "))
    if x < 0 :
        break
    number.append(x)

print(f"Before sort : {number}")
number.sort() # small to big
print(f"After sort : {number}")
number.reverse() #big to small
print(f"After reverse : {number}")
