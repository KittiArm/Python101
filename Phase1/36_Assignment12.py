# Assignment12
# Find Greatest and Least number

max, min = 0, 9999999999999

while True:
    number =int(input("Enter number : "))
    if number<0:
        break
    if number>max:
        max=number
    if number<min:
        min=number
print(f"Min = {min}, Max = {max}")