# Assignment20

number = []
_even = []
_odd = []
while True:
    x = int(input("Enter your single number : "))
    if x < 0 :
        break
    if x%2 == 0:
        _even.append(x)
        number.append(x)
    else:
        _odd.append(x)
        number.append(x)

print(f"All number list : {number}")
print(f"Even number list : {_even}")
print(f"Odd number list : {_odd}")