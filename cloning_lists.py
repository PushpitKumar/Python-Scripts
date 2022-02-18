#If we want to modify a list and also keep a copy of the original, we need to be able to make a copy of the list itself, not just the reference. This process is sometimes called cloning, to avoid the ambiguity of the word copy.
#The easiest way to do this is using the slice operator.

a = [81,82,83]
b = a[:] #Taking any slice of 'a' creates a new list. In this case, slice happens to consist of the whole list 'a'
print(a==b)
print(a is b)

b[0] = 5 #a will not change now since b is a diferent list now.

print(a)
print(b)
