a = 'banana'
b = 'banana'

print(a is b) #Evaluates to true because both a and b refer to the same object that has the value banana
print(a==b) #True. Always use this for comparison but don't be surprised when two variables haing same values have the same id.
#Python assigns every object a unique id and when we ask if 'a is b', it is checking whether id(a)==id(b)
print(id(a))
print(id(b))
#Since strings are immutable, the Python interpreter often optimizes resources by making two names that refer to the same string value refer to the same object.

#This is not the case with lists, which never share an id just because they have the same contents.
lst = [1,2,3]
lst2 = [1,2,3]

print(lst is lst2)
print(lst==lst2)

print(id(lst))
print(id(lst2))

#lst and lst2 have equivalent values but do not refer to the same object. Because their contents are equivalent, lst==lst2 evaluates to True; because they are not the same object, lst is lst2 evaluates to False.
