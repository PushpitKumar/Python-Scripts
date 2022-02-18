#Write a program that finds the key in a dictionary that has the maximum value. If two keys have the same maximum value, it’s OK to print out either one.
d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}
keys = list(d.keys())
best_key_so_far = keys[0]
for key in keys:
    if d[key] > d[best_key_so_far]:
        best_key_so_far = key
print('key',best_key_so_far,'has the highest value of',str(d[best_key_so_far]))
