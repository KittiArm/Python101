# Comparison
'''
1.Take at least 2 variables fo comparing
2.Two variables must be the same data type
3.Comparing result will be boolean >> there are only True, False
'''

x, y = 10, 5

print("x is greater than y :", x > y)
print("x is less than y :", x < y)

print("x is equal to y :", x == y)
print("x is not equal to y :", x != y)

print("x is greater than or equal to y :", x >= y)
print("x is less than or equal to y :", x <= y)

z = 9
print("x is greater than y and y is greater than z:", x > y > z)
print("x is greater than y and y is greater than z:", x > y & y > z)