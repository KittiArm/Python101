# Assignment8
# Calculate summation of number

i=1
summation = 0
averge = 0

count = int(input("Enter number of round : "))

while i<=count:
    summation+=i
    print(f"Round : {i}, Summation = {summation}")
    i+=1
print(f"Summation = {summation}")
print(f"Average = {summation/count}")