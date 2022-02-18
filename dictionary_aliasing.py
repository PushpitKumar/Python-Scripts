#Because dictionaries are mutable, you need to be aware of aliasing (as we saw with lists). Whenever two variables refer to the same dictionary object, changes to one affect the other. For example, opposites is a dictionary that contains pairs of opposites.
opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)

alias['right'] = 'left'
print(opposites['right'])

#If you want to modify a dictionary and keep a copy of the original, use the dictionary copy method. Since acopy is a copy of the dictionary, changes to it will not effect the original.
opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
acopy = opposites.copy()
acopy['right'] = 'left'  #does not change opposites
print(opposites)
print(acopy)
