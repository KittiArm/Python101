# Operator priority in math
'''
Parentheses >> Unary operator >> Multiplication, Division od Molulus >> Addition and Subtraction >> Assignment (Multiple)

() >> -, +, --, ++, sizeof, (type) >> *, / or % >> + or - >> =
'''

a = 5 + 2 * 10 / 2
print(a)

b = 5 + 2 / 10 * 2
print(b)

c = (5 + 2)/10 * 2
print(c)

d = (5 + 2)/(10 * 2)
print(d)