# Break / Continue

i=0
print("Break in loop")
while i<=10:
    print(f"Round {i}")
    if i==5:
        break
    i+=1
print("Process was end")

i=0
print("Countinue in loop")
while i<=10:
    i+=1
    if i%2 != 0:
        continue
    print(f"Round {i}")
print("Process was end")