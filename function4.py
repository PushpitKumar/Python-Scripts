#Not only can you pass a parameter value into a function, a function can also produce a value. You have already seen this in some previous functions that you have used. For example, len takes a list or string as a parameter value and returns a number, the length of that list or string. range takes an integer as a parameter value and returns a list containing all the numbers from 0 up to that parameter value.
#Functions that return values are sometimes called fruitful functions. In many other languages, a function that doesn’t return a value is called a procedure, but we will stick here with the Python way of also calling it a function, or if we want to stress it, a non-fruitful function.
def square(x):
    y = x * x
    return y

toSquare = 10
result = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, result))

#The return statement is followed by an expression which is evaluated. Its result is returned to the caller as the “fruit” of calling this function. Because the return statement can contain any Python expression we could have avoided creating the temporary variable y and simply used return x*x.
#Using temporary variables like y in the program above makes debugging easier. These temporary variables are referred to as local variables.

#There is one more aspect of function return values that should be noted. All Python functions return the special value None unless there is an explicit return statement with a value other than None.

def square2(x):
    y = x*x
    print(y)

toSquare = 10
squareResult = square2(toSquare)
print("The result of {} squared is {}.".format(toSquare, squareResult))
#The problem with this function is that even though it prints the value of the squared input, that value will not be returned to the place where the call was done. Instead, the value None will be returned. Since line 6 uses the return value as the right hand side of an assignment statement, squareResult will have None as its value and the result printed in line 7 is incorrect. Typically, functions will return values that can be printed or processed in some other way by the caller.

#A return statement, once executed, immediately terminates execution of a function, even if it is not the last statement in the function. In the following code, when line 3 executes, the value 5 is returned and assigned to the variable x, then printed. Lines 4 and 5 never execute.
def weird():
    print("here")
    return 5
    print("there")
    return 10

x = weird()
print(x)

#The fact that a return statement immediately ends execution of the code block inside a function is important to understand for writing complex programs, and it can also be very useful.
#Consider a situation where you want to write a function to find out, from a class attendance list, whether anyone’s first name is longer than five letters, called longer_than_five. If there is anyone in class whose first name is longer than 5 letters, the function should return True. Otherwise, it should return False.
