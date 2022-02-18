#Sometimes it is convenient to have optional parameters that can be specified or omitted. When an optional parameter is omitted from a function invocation, the formal parameter is bound to a default value. When the optional parameter is included, then the formal parameter is bound to the value provided. Optional parameters are convenient when a function is almost always used in a simple way, but it’s nice to allow it to be used in a more complex way, with non-default values specified for the optional parameters.
#The int function provides an optional parameter for the base. When it is not specified, the number is converted to an integer assuming the original number was in base 10. We say that 10 is the default value. So int("100") is the same as invoking int("100", 10). We can override the default of 10 by supplying a different value.
print(int('100'))
print(int('100',10)) #same thing, 10 is the default value for base
print(int('100',8)) #now the base is 8, so the result is 1*64 = 64

#When defining a function, you can specify a default value for a parameter. That parameter then becomes an optional parameter when the function is called. The way to specify a default value is with an assignment statement inside the parameter list. Consider the following code, for example.
initial = 7
def f(x,y=3,z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))
f(2)
f(2,5)
f(2,5,8)
#Notice the different bindings of x, y, and z on the three invocations of f. The first time, y and z have their default values, 3 and 7. The second time, y gets the value 5 that is passed in, but z still gets the default value of 7. The last time, z gets the value 8 that is passed in.
#If you want to provide a non-default value for the third parameter (z), you also need to provide a value for the second item (y). We will see in the next section a mechanism called keyword parameters that lets you specify a value for z without specifying a value for y.
#This is a second, related but slightly different use of = than we have seen previously. In a stand-alone assignment statement, not part of a function definition, x=3 assigns 3 to the variable x. As part of specifying the parameters in a function definition, x=3 says that 3 is the default value for x, used only when no value is provided during the function invocation.
#There are two tricky things that can confuse you with default values. The first is that the default value is determined at the time that the function is defined, not at the time that it is invoked. So in the example above, if we wanted to invoke the function f with a value of 10 for z, we cannot simply set initial = 10 right before invoking f. See what happens in the code below, where z still gets the value 7 when f is invoked without specifying a value for z.
initial = 7
def f(x, y =3, z=initial):
	print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))
initial = 10
f(2)

#The second tricky thing is that if the default value is set to a mutable object, such as a list or a dictionary, that object will be shared in all invocations of the function. This can get very confusing, so I suggest that you never set a default value that is a mutable object. For example, follow the exceution of this one carefully.
def f(a, L=[]):
	L.append(a)
	return L
print(f(1))
print(f(2))
print(f(3))
print(f(4, ["Hello"]))
print(f(5, ["Hello"]))
#When the default value is used, the same list is shared. But on lines 7 and 8 two different copies of the list [“Hello”] are provided, so the 4 that is appended is not present in the list that is printed on line 8.

#Write a function called str_mult that takes in a required string parameter and an optional integer parameter. The default value for the integer parameter should be 3. The function should return the string multiplied by the integer parameter.
def str_mult(string,x=3):
    return string*x
print(str_mult('Lucatiel'))
print(str_mult('DS',5))
