#The basic idea of passing arguments by keyword is very simple. When invoking a function, inside the parentheses there are always 0 or more values, separated by commas. With keyword arguments, some of the values can be of the form paramname = <expr> instead of just <expr>. Note that when you have paramname = <expr> in a function definition, it is defining the default value for a parameter when no value is provided in the invocation; when you have paramname = <expr> in the invocation, it is supplying a value, overriding the default for that paramname.
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
	print("-- This parrot wouldn't" + action,)
	print("if you put" + str(voltage) + "volts through it.")
	print("-- Lovely plumage, the" +  type)
	print("-- It's " + state + "!")
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#Note that we have yet another, slightly different use of the = sign here. As a stand-alone, top-level statement, x=3, the variable x is set to 3. Inside the parentheses that invoke a function, x=3 says that 3 should be bound to the local variable x in the stack frame for the function invocation. Inside the parentheses of a function definition, x=3 says that 3 should be the value for x in every invocation of the function where no value is explicitly provided for x.

#Keyword parameters with .format method
names_scores = [('Jack',[67,89,91]),('Emily',[72,95,42]),('Taylor',[83,92,86])]
for name,scores in names_scores:
    print('The scores {nm} got were: {s1}, {s2} and {s3}'.format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))

#Sometimes, you may want to use the .format method to insert the same value into a string multiple times. You can do this by simply passing the same string into the format method, assuming you have included {} s in the string everywhere you want to interpolate them. But you can also use positional passing references to do this! The order in which you pass arguments into the format method matters: the first one is argument 0, the second is argument 1, and so on.
#For Example,

# this works
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))
