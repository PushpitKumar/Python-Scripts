#We can use append or concatenate repeatedly to create new objects. If we had a string and wanted to make a new list. we can do so like this using append as shown below
st = 'warmth'
lst = list(st) #simplest way
print(lst)
#or we can do so using a loop
a = list()
for char in st:
    a.append(char)
print(a)
#We can also use concatenate method to create the list
b = list()
for char in st:
    b = b + [char]
print(b)
