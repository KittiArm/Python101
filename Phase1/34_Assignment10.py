# Assignment10
start, stop = 1, 5
sum, avg = 0, 0
while start<=stop:
    number = int(input("Enter number : "))
    sum+=number
    start+=1
print(f"Summation = {sum}")
print(f"Average = {sum/stop}")
