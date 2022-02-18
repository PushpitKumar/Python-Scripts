#Python even provides a way to pass a single tuple to a function and have it be unpacked for assignment to the named parameters.
def add(x, y):
    return x + y
print(add(3, 4))
z = (5, 4)
#print(add(z)) ---> this line causes an error

#This won’t quite work. It will cause an error, because the function add is expecting two parameters, but you’re only passing one parameter (a tuple). If only there was a way to tell python to unpack that tuple and use the first element to assign to x and the second to y. Actually, there is a way.
def add(x, y):
    return x + y
print(add(3, 4))
z = (5, 4)
print(add(*z)) # this line will cause the values to be unpacked

#Use a for loop to print out the last name, year of birth, and city for each of the people. (There are multiple ways you could do this. Try out some code and see what happens!)
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
claude = ("Claude", "Shannon", 1916, "A Mathematical Theory of Communication", 1948, "Mathematician", "Petoskey, Michigan")
alan = ("Alan", "Turing", 1912, "Computing machinery and intelligence", 1950, "Mathematician", "London, England")

People = [julia,claude,alan]
for details in People:
    print(details[1],details[2],details[6])

#With only one line of code, assign the variables city, country, and year to the values of the tuple olymp.
olymp = ('Rio','Brazil',2016)
city,country,year = olymp
