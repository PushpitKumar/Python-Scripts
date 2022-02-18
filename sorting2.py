#Optional reverse parameter
#The sorted function takes some optional parameters (see the Optional Parameters page). The first optional parameter is a key function, which will be described in the next section. The second optional parameter is a Boolean value which determines whether to sort the items in reverse order. By default, it is False, but if you set it to True, the list will be sorted in reverse order.
L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))

#Sort the list, lst from largest to smallest. Save this new list to the variable lst_sorted.
lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst,reverse=True)
print(lst_sorted)

#Optional key parameter
#If you want to sort things in some order other than the “natural” or its reverse, you can provide an additional parameter, the key parameter. For example, suppose you want to sort a list of numbers based on their absolute value, so that -4 comes after 3? Or suppose you have a dictionary with strings as the keys and numbers as the values. Instead of sorting them in alphabetic order based on the keys, you might like to sort them in order based on their values.
#First, let’s define a function absolute that takes a number and returns its absolute value. (Actually, python provides a built-in function abs that does this, but we are going to define our own, for reasons that will be explained in a minute.)
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    return -x

print(absolute(3))
print(absolute(-119))

for y in L1:
    print(absolute(y))

#Now, we can pass the absolute function to sorted in order to specify that we want the items sorted in order of their absolute value, rather than in order of their actual value.
L3 = [1,7,4,-2,3]
L4 = sorted(L3,key=absolute)
print(L4)

#or in reverse order
print(sorted(L1, reverse=True, key=absolute))

#What’s really going on there? We’ve done something pretty strange. Before, all the values we have passed as parameters have been pretty easy to understand: numbers, strings, lists, Booleans, dictionaries. Here we have passed a function object: absolute is a variable name whose value is the function. When we pass that function object, it is not automatically invoked. Instead, it is just bound to the formal parameter key of the function sorted.
#We are not going to look at the source code for the built-in function sorted. But if we did, we would find somewhere in its code a parameter named key with a default value of None. When a value is provided for that parameter in an invocation of the function sorted, it has to be a function. What the sorted function does is call that key function once for each item in the list that’s getting sorted. It associates the result returned by that function (the absolute function in our case) with the original value. Think of those associated values as being little post-it notes that decorate the original values. The value 4 has a post-it note that says 4 on it, but the value -2 has a post-it note that says 2 on it. Then the sorted function rearranges the original items in order of the values written on their associated post-it notes.
#To illustrate that the absolute function is invoked once on each item, during the execution of sorted, I have added some print statements into the code.
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    print("--- figuring out what to write on the post-it note for " + str(x))
    if x >= 0:
        return x
    else:
        return -x

print("About to call sorted")
L2 = sorted(L1, key=absolute)
print("Finished execution of sorted")
print(L2)
#Note that this code never explicitly calls the absolute function at all. It passes the absolute function as a parameter value to the sorted function. Inside the sorted function, whose code we haven’t seen, that function gets invoked.
#It is a little confusing that we are reusing the word key so many times. The name of the optional parameter is key. We will usually pass a parameter value using the keyword parameter passing mechanism. When we write key=some_function in the function invocation, the word key is there because it is the name of the parameter, specified in the definition of the sort function, not because we are using keyword-based parameter passing.

# You will be sorting the following list by each element’s second letter, a to z. Create a function to use when sorting, called second_let. It will take a string as input and return the second letter of that string. Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. Do not use lambda.
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(string):
    return string[1]
sorted_by_second_let = sorted(ex_lst,key=second_let)
print(sorted_by_second_let)

#Below, we have provided a list of strings called nums. Write a function called last_char that takes a string as input, and returns only its last character. Use this function to sort the list nums by the last digit of each number, from highest to lowest, and save this as a new list called nums_sorted.
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(string):
    return string[-1]
nums_sorted = sorted(nums,reverse=True,key=last_char)
print(nums_sorted)

#Once again, sort the list nums based on the last digit of each number from highest to lowest. However, now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.
last_char1 = lambda string: string[-1]
nums_sorted1 = sorted(nums,reverse=True,key=last_char)
print(nums_sorted1)
