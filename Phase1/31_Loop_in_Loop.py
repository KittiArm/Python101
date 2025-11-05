# Loop in loop

# While in while
i=1
print("While in while")
while i<=3:
    print(f"Roung {i}")
    j=1
    while j<=5:
        print(f"Position {j}")
        j+=1
    i+=1
print("Process was end")

# For in for
print("For in for")
for m in range(1, 4):
    print(f"Round {m}")
    for n in range (1, 6):
        print(f"Position {n}")
print("Process was end")        