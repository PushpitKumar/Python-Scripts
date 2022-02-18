#Anonymous functions with lambda expressions
#To further drive home the idea that we are passing a function object as a parameter to the sorted object, let’s see an alternative notation for creating a function, a lambda expression. The syntax of a lambda expression is the word “lambda” followed by parameter names, separated by commas but not inside (parentheses), followed by a colon and then an expression. lambda arguments: expression yields a function object. This unnamed object behaves just like the function object constructed below.
def f_name(arguments):
    return expression

#f_name = lambda arguments: return expression

#Consider the following code:
def f(x):
    return x-1
print(f)
print(type(f))
print(f(3))

print(lambda x: x-2)
print(type(lambda x: x-2))
print((lambda x: x-2)(6))

lambda_function = lambda y: y-2
print(lambda_function)
print(type(lambda_function))
print(lambda_function(5))

#A function, whether named or anonymous, can be called by placing parentheses () after it. In this case, because there is one parameter, there is one value in parentheses. This works the same way for the named function and the anonymous function produced by the lambda expression. The lambda expression had to go in parentheses just for the purposes of grouping all its contents together.

#Say we want to create a function that takes a string and returns the last character in that string.
def last_char(string):
    return string[-1]
print(last_char('Clare'))

last_char_lambda = lambda string: string[-1]
print(last_char_lambda('Clare'))
#In the typical function, we have to use the keyword return to send back the value. In a lambda function, that is not necessary - whatever is placed after the colon is what will be returned.
