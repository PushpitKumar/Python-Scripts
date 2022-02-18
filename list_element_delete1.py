#Delete elemnts in a list by assigning them empty list
a = [1,2,3,4,5,6,7,9]
a[4:5] = []

b = [0,4,8,3,99,11,43,76,64]
b[1:4] = []

c = [100,200,300,400,500,600]
c[5:5] = [] #Nothing happens

print(a)
print(b)
print(c)
