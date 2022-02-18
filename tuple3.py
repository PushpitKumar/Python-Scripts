#Functions can return tuples as return values. This is very useful — we often want to know some batsman’s highest and lowest score, or we want to find the mean and the standard deviation, or we want to know the year, the month, and the day, or if we’re doing some ecological modeling we may want to know the number of rabbits and the number of wolves on an island at a given time. In each case, a function (which can only return a single value), can create a single tuple holding multiple elements.
def CircleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)
print(CircleInfo(10))

#Again, we can take advantage of packing to make the code look a little more readable on line 4.
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

print(circleInfo(10))

#It’s common to unpack the returned values into multiple variables.
circumference, area = CircleInfo(10)
print(circumference)
print(area)

circumference_two, area_two = circleInfo(45)
print(circumference_two)
print(area_two)

#Define a function called information that takes as input, the variables name, birth_year, fav_color, and hometown. It should return a tuple of these variables in this order.
def information(name,birth_year,fav_color,hometown):
    return (name,birth_year,fav_color,hometown)
print(information('Pushpit',1999,'Red','Bihar Shariff'))
