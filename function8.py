#It is important to understand that each of the functions we write can be used and called from other functions we write. This is one of the most important ways that computer programmers take a large problem and break it down into a group of smaller problems. This process of breaking a problem into smaller subproblems is called functional decomposition.
def square(x):
    y = x*x
    return y
def sum_of_squares(x,y,z):
    a = square(x)
    b = square(y)
    c = square(z)
    return a+b+c

a = -5
b = 2
c = 10
result = sum_of_squares(a,b,c)
print(result)
#Each group of local variables is called a stack frame. The variables x, and y are local variables in both functions. These are completely different variables, even though they have the same name. Each function invocation creates a new frame, and variables are looked up in that frame.

#Accumulate a dictionary with letters as keys and counts as values and find the best key from that dictionary.
def letter_frequency(string):
    d = {}
    for char in string:
        if char not in d:
            d[char] = 0
        d[char] = d[char] + 1
    return d

def best_key(dictionary):
    ks = list(dictionary.keys())
    best_key_so_far = ks[0]
    for key in ks:
        if dictionary[key] > dictionary[best_key_so_far]:
            best_key_so_far = key
    return best_key_so_far

def most_common_letter(letter):
    frequencies = letter_frequency(letter)
    return best_key(frequencies)
print(most_common_letter("abbbbbbbbbbbccccddddd"))

#Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.
def addit(num):
    return num + 5
def mult(num1):
    c = num1 * addit(num1)
    return c
print(mult(2))
