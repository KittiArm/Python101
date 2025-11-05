# Dictionary => key (access), value (data value)

member = {"Gender":["Male","Female"], "City":["Bangkok","Pathumthani"]}
print(member["Gender"])

room = dict({301:"Mr. A", 302:"Mr. B", 303:"Mr, C"})
print(room[302])
print(room.get(303))

room[301]="UUUU"
print(room[301])

room.update({304:"MMM"})
print(room)

for item in room.keys():
    print(item)

for item in room.values():
    print(item)

for k, v in room.items():
    print(f"Keys = {k}, Values ={v}")

print("Pop >>>")
print(f"Before {room}")
room.pop(301) # Remove data at Keys
print(f"After {room}")

print("Popitem >>>")
print(f"Before {room}") # Remove the lastest item
room.popitem()
print(f"After {room}")

print("Clear >>>")
print(f"Before {room}") # Remove the lastest item
room.clear()
print(f"After {room}")

# Nested Dictionary
print("Dict in dict >>>")
market = {
    "Pathumthani":{
        "Department Store":"Future Park",
        "member":2000,
        "open":"10.00 A.M."
    },
    "Bangkok":{
        "Department Store":"Central World",
        "member":6000,
        "open":"10.00 A.M."
    }
}
print(market)

print("10.00 A.M." in market["Bangkok"]["open"])

if "10.00 A.M." in market["Bangkok"]["open"]:
    print("Yes")
else:
    print("No")