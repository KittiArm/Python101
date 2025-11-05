# Pass : skip statement of expression

age = int(input("Plaes enter your age : "))

if age<=15:
    if age==15:
        print("Junior high school Grade 9")
    elif age==14:
        pass
    elif age==13:
        pass
    else:
        print("Elementary")
else:
    print("high school")