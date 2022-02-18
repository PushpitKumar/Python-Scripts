#Define a function called nums that has three parameters. The first parameter, an integer, should be required. A second parameter named mult_int should be optional with a default value of 5. The final parameter, switch, should also be optional with a default value of False. The function should multiply the two integers together, and if switch is True, should change the sign of the product before returning it.
def nums(x,mult_int=5,switch=False):
    if switch is True:
        return -(x*mult_int)
    return x*mult_int
print(nums(4))
print(nums(3,3,False))
print(nums(5,2,True))

#Write a function called together that takes three parameters, the first is a required parameter that is a number (integer or float), the second is a required parameter that is a string, and the third is an optional parameter whose default is ” “. What is returned is the first parameter, concatenated with the second, using the third.
def together(num,string,c=" "):
    return str(num) + c + string
print(together(1,'ring to rule them all'))
print(together(9,'rings were given to the race of men',' powerful '))

#Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.
def test(num,switch=True,dict1={2:3,4:5,6:8}):
    if switch is True:
        if num in dict1:
            return dict1[num]
    return False
print(test(3))
print(test(4,True))
print(test(5,False,{5:6,6:7,7:8}))
print(test(5,True,{5:6,6:7,7:8}))

#Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.
#But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is, it should return False.
def checkingIfIn(string,direction=True,d={'apple':2,'pear':1,'fruit':19,'orange':5,'banana':3,'grapes':2,'watermelon':7}):
    if direction is True:
        if string in d:
            return True
        return False
    if string not in d:
        return True
    return False
print(checkingIfIn('orange'))
