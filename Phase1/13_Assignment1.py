# Assignment1
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
print("Your BMI is :", bmi)