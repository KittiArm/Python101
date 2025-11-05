# Assignment6
# BMI Program
# BMI = Weight:kg / Sqr(Height:m)

# Input and convert data type
weight = float(input("Please enter your weight (kg) : "))
height = float(input("Please enter your height (cm) : "))

# Process
# Change unit of height
height /= 100

# Calculate BMI
bmi = weight/(height**2)

# Output
if bmi<18:
    result = "skinny"
elif bmi>=18.5 and bmi<=22.9:
    result = "Thin"
elif bmi>22.9 and bmi<=24.9:
    result = "normal"
elif bmi>24.9 and bmi<=29.9:
    result = "overweight"
else:
    result = "Obesity"

print("Your BMI = ", bmi, ", you're", result)