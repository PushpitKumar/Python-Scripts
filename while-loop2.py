#Using a while loop, create a list numbers that contains the numbers 0 through 35. Your while loop should initialize a counter variable to 0. On each iteration, the loop should append the current value of the counter to the list and the counter should increase by 1. The while loop should stop when the counter is greater than 35.
i = 0
numbers = list()
while i <= 35:
    numbers.append(i)
    i+=1
print(numbers)

#Create a while loop that initializes a counter at 0 and will run until the counter reaches 50. If the value of the counter is divisible by 10, append the value to the list, tens.
i = 0
tens = list()
while i<=50:
    if i%10==0:
        tens.append(i)
    i+=1
print(tens)

#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
def sublist(lst):
    new_lst = []
    i = 0
    while i < len(lst):
        if lst[i] == 5:
            break
        new_lst.append(lst[i])
        i+=1
    return new_lst
print(sublist([1,2,3,4,6,7,8,9,10,5]))

#Write a function, sublist1, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
def sublist1(lst):
    new_lst = []
    i = 0
    while i < len(lst):
        if lst[i] == 'STOP':
            break
        new_lst.append(lst[i])
        i+=1
    return new_lst
print(sublist1(['Ana','Lisa','Havana','Shira','STOP','Filianore','Gwynevere']))

#Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.). If you want to make this even more of a challenge, do this without slicing
def beginning(lst):
    new_lst = []
    i = 0
    while i < 10:
        if lst[i] == 'bye':
            break
        new_lst.append(lst[i])
        i+=1
    return new_lst
print(beginning(['Hello','DS','DS2','DS3','BB','bye','Sekiro']))
print(beginning(['bye','hello','a','b','c']))
print(beginning(['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']))

##Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.).
def beginning1(lst):
    i = 0
    new_list = []
    while i < len(lst):
        if lst[i] == 'bye':
            break
        new_list.append(lst[i])
        i+=1
    return new_list[:10] #Using slicing method
print(beginning1(['Hello','DS','DS2','DS3','BB','bye','Sekiro']))
print(beginning1(['h','i','ii','u','hello','v','c','b','gg','ss','hola','clown','kk','bye','never','again']))
