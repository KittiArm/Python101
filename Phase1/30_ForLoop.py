# for loop
# for i in range(start, stop, step)
# range(n) : start at 0 end n-1

 # start at 0 end at 2 (0-1-2)
for i in  range(3): 
    print(f"Round {i}, Hello World")
print("Process was end.")

 # start at 2 end at 4 (2-3-4)
for i in  range(2, 5):
    print(f"Round {i}, Hello World")
print("Process was end.")

 # start at 0 end at 9 step 2 (0-2-4-6-8)
for i in range(0,10,2):
    print(f"Round {i}, Hello World")
print("Process was end.")

# summation
summation = 0
for i in range(1, 6):
    summation+=i
    print(f"Round : {i}, Summation : {summation}")

print("Process was end.")