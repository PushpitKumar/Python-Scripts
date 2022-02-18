#In the definition, the parameter list is sometimes referred to as the formal parameters or parameter names. These names can be any valid variable name. If there is more than one, they are separated by commas.
#In the function invocation, inside the parentheses one value should be provided for each of the parameter names. These values are separated by commas. The values can be specified either directly, or by any python expression including a reference to some other variable name.
def hello(s):
    print("Hello " + s)
	print("Glad to meet you")

hello("Iman")
hello("Jackie")

def hello2(s,n):
    greeting = 'Hello {} '.format(s)
    print(greeting*n)

hello2('Wei',4)
hello2('',1)
hello2('Kitty',11)
