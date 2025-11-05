# Set >> set is frozen : must not have the same data

_set_a = {0, 1, 3, 5, 5, 7, 9}
_set_b = {0, 2, 4, 6, 8}
print(_set_a)
print(_set_b)

_set_a = set([0, 1, 3, 5, 7, 9])
_set_b = set([0, 2, 4, 6, 8])

_set_a.add(10)
print(f"Add = {_set_a}")

_set_a.update([100, 200, 300])
print(f"Update = {_set_a}")

for iten in _set_a:
    print(f"Data : {iten}")

_set_a.discard(999)
print(f"Discard = {_set_a}")