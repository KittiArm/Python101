# Assignment7
# Convert temperature unit
# F to C : c = (f-32)*(5/9)
# C to F : f = (c*9/5)+32

temp = input("Enter temperature (degree) : ")

itemp = float(temp[:-1])
unit = str(temp[-1].upper())

if unit=="F":
    funit = "C"
    ftemp = (itemp-32)*(5/9)
elif unit=="C":
    funit = "F"
    ftemp = (itemp*9/5)+32
print(f"{itemp} {unit} = {ftemp} {funit}")

