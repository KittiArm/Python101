# Assignment4
# Banknote Separator Program

# 2000 => 1000 = 2 
# 1500 => 1000 = 1, 500 = 1
# 1800 => 1000 = 1, 500 = 1, 100 = 3
# 100 => 50 = 2

number = int(input("Enter your money value : "))

if number>=1000:
    print("1000 THB =", number//1000)
    number = number%1000
if number>=500:
    print("500 THB =", number//500)
    number = number%500
if number>=100:
    print("100 THB =", number//100)
    number = number%100
if number>=50:
    print("50 THB =", number//50)
    number = number%50
if number>=20:
    print("20 THB =", number//20)
    number = number%20
if number>=10:
    print("10 THB =", number//10)
    number = number%10
if number>=5:
    print("5 THB =", number//5)
    number = number%5
if number>=2:
    print("2 THB =", number//2)
    number = number%2
if number>=1:
    print("1 THB =", number//1)