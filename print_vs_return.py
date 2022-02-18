#The print statement is fairly easy to understand. It takes a python object and outputs a printed representation of it in the output window. You can think of the print statement as something that takes an object from the land of the program and makes it visible to the land of the human observer.
#Print is for people. Remember that slogan. Printing has no effect on the ongoing execution of a program. It doesn’t assign a value to a variable. It doesn’t return a value from a function call.
#A function that returns a value is producing a value for use by the program, in particular for use in the part of the code where the function was invoked. Remember that when a function is invoked, the function’s code block is executed – all that code indented under the def statement gets executed, following the rules of the Python formal language for what should and should not execute as it goes. But when the function returns, control goes back to the calling location, and a return value may come back with it.
#If your only purpose in running a function is to make an output visible for human consumption, there are two ways to do it. You can put one or more print statements inside the function definition and not bother to return anything from the function (the value None will be returned). In that case, invoke the function without a print statement. For example, you can have an entire line of code that reads f(3). That will run the function f and throw away the return value. Of course, if square doesn’t print anything out or have any side effects, it’s useless to call it and do nothing with the return value. But with a function that has print statements inside it, it can be quite useful.
#The other possibility is to return a value from the function and print it, as in print(f(3)). As you start to write larger, more complex programs, this will be more typical. Indeed the print statement will usually only be a temporary measure while you’re developing the program. Eventually, you’ll end up calling f and saving the return value or using it as part of a more complex expression.
def square(x):
    return x*x

def g(y):
    return y + 3

def h(y):
    return square(y) + 3

print(h(2))
print(g(h(2)))
