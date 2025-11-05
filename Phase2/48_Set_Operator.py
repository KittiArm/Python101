# Set Operatoe >> must not have the same data

_set_a = {0, 1, 3, 5, 5, 7, 9}
_set_b = {0, 2, 4, 6, 8}


_set_a = set([0, 1, 3, 5, 7, 9])
_set_b = set([0, 2, 4, 6, 8])
_union = _set_a.union(_set_b)
_intersection = _set_a.intersection(_set_b)
_differance1 = _set_a.difference(_set_b) # a-b
_differance2 = _set_b.difference(_set_a) # b-a

print(f"Set A = {_set_a}")
print(f"Set B = {_set_b}")
print(f"Union = {_union}")
print(f"Intersection = {_intersection}")
print(f"Difference A-B = {_differance1}")
print(f"Difference B-A = {_differance2}")
