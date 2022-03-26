d = {1: [10], 2: [15], 3: [20], 4: [3333], 8: [], 64: [99996666]}
key = 10
value = 123456789
if d.get(key) in d.values():
    d[key].append(value)
elif d.get(key) not in d.values():
    if d.get(2 * key) in d.values():
        d[2 * key].append(value)
    else:
        d[2 * key] = [value]

print(d)

# def update_dictionary(d, key, value):
#    if d.get(key) in d:
#       d[key] = value
