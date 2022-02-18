#Python has a very powerful tuple assignment feature that allows a tuple of variable names on the left of an assignment statement to be assigned values from a tuple on the right of the assignment. Another way to think of this is that the tuple of values is unpacked into the variable names.
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
name, surname, birth_year, movie, movie_year, profession, birth_place = julia
#This does the equivalent of seven assignment statements, all on one easy line. Naturally, the number of variables on the left and the number of values on the right have to be the same.

#(a, b, c, d) = (1, 2, 3) --> ValueError: need more than 3 values to unpack
#Unpacking into multiple variable names also works with lists, or any other sequence type, as long as there is exactly one value for each variable. For example, you can write x, y = [3, 4].

#This feature is used to enable swapping the values of two variables. With conventional assignment statements, we have to use a temporary variable. For example, to swap a and b:
a = 1
b = 2
temp = a
a = b
b = temp
print(a,b,temp)

#Tuple assignment solves this problem neatly:
a = 1
b = 2
a,b = b,a
print(a,b)
#The left side is a tuple of variables; the right side is a tuple of values. Each value is assigned to its respective variable. All the expressions on the right side are evaluated before any of the assignments. This feature makes tuple assignment quite versatile.

#Multiple assignment with unpacking is particularly useful when you iterate through a list of tuples. You can unpack each tuple into several loop variables. For example:
authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)
#On the first iteration the tuple ('Paul', 'Resnick') is unpacked into the two variables first_name and last_name. One the second iteration, the next tuple is unpacked into those same loop variables.

#Enum
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

#A better way to to this is using enum. Python provides a built-in function enumerate. It takes a sequence as input and returns a sequence of tuples. In each tuple, the first element is an integer and the second is an item from the original sequence. (It actually produces an “iterable” rather than a list, but we can use it in a for loop as the sequence to iterate over.)
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for item in enumerate(fruits):
    print(item[0], item[1])

#The pythonic way to consume the results of enumerate, however, is to unpack the tuples while iterating through them, so that the code is easier to understand.
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

#With only one line of code, assign the variables water, fire, electric, and grass to the values “Squirtle”, “Charmander”, “Pikachu”, and “Bulbasaur”
water,fire,electric,grass = 'Squirtle','Charmander','Pikachu','Bulbasaur'

#If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided you a dictionary called pokemon. For every key value pair, append the key to the list p_names, and append the value to the list p_number. Do not use the .keys() or .values() methods.
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = list()
p_number = list()
for item in pokemon.items():
    p_names.append(item[0])
    p_number.append(item[1])
print(p_names)
print(p_number)
