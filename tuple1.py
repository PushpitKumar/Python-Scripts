#Wherever python expects a single value, if multiple expressions are provided, separated by commas, they are automatically packed into a tuple. For example, we can omit the parentheses when assigning a tuple of values to a single variable.
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# or equivalently
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
print(julia[4])

#Create a tuple called practice that has four elements: ‘y’, ‘h’, ‘z’, and ‘x’.
practice = ('y','h','z','x')
print(practice)
#Create a tuple named tup1 that has three elements: ‘a’, ‘b’, and ‘c’.
tup1 = 'a','b','c'
print(tup1)

# Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = list()
for tup in lst_tups:
    t_check.append(tup[2])
print(t_check)
