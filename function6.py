#Write a function named same that takes a string as input, and simply returns that string.
def same(string):
    return string
print(same('Elden Ring'))

#Write a function named intro that takes a string as input. Given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”
def intro(name):
    return 'Hello, my name is {} and I love SI 106'.format(name)
print(intro('Lowly Tarnished'))

#Write a function called decision that takes a string as input, and then checks the number of characters. If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.
def decision(string):
    if len(string) > 17:
        return 'This is a long string'
    return 'This is a short string'
print(decision('A lowly tarnished playing as a lord? I command thee kneel!'))

#Create your own len function
def mylen(sequence):
    count = 0
    for _ in sequence:
        count+=1
    return count
print(mylen('Elden Ring'))
print(mylen(['j',1,2,3,4,'Poop']))
