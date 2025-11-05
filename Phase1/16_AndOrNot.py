# Logical Operator(and, or, not) in Seleccted Control Structure

age = int(input("Pleasee enter your age : "))

if age >= 15 and age < 20:
    print("Teenager")
elif age >= 20 and age <30:
    print("Adult")
elif age >= 30 and age < 60:
    print("Worker")
elif age > 60:
    print("Elder")
else:
    print("Kid")

print("Process was end.")