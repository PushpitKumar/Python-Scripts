#Since variables refer to objects, if we assign one variable to another, both variables refer to the same object.
a = [81,82,83]
b = a
print(a is b)

#Because the same list has two different names, a and b, we say that it is aliased. Changes made with one alias affect the other.

print(a==b)
b[0] = 5
print(a)

#Although this behavior can be useful, it is sometimes unexpected or undesirable. In general, it is safer to avoid aliasing when you are working with mutable objects. Of course, for immutable objects, there’s no problem. That’s why Python is free to alias strings and integers when it sees an opportunity to economize.
w = ['Jamboree', 'get-together', 'party']
y = ['celebration']
y = w
print(w)
w = y
print(y) ##Now y will hold w's value. Therefore 'celebration' is lost forever!
