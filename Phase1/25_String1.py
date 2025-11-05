name = " KITTIPONG CHANKHOTR " # index start at 0

name[1:15] # Literal access : select start at 0 to before 3
len(name) # len(variable) : count the number of letter

name.strip() # variable.strip() : Eliminate space
name.lstrip() # variable.lstrip() : Eliminate left space
name.rstrip() # variable.rstrip() : Eliminate right space

name.upper() # variable.upper() : change string to be uppercase
name.lower() # variable.lower() : change string to be lowercase

name.capitalize() # variable.capitalize() : change first character to be uppercase

name.replace("T", "5", 1) # variable.replace("old", "new", number) : replace "old" with "new" by number

x = "PONG" in name # "word" in variable : check "word" in variable, result will be boolean(True/False).

print(x)