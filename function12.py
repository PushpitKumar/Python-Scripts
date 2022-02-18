#Write a function that will return the number of digits in an integer.
def len_num(number):
    return len(str(number))
print(len_num(100))

#Write a function that mirrors its string argument, generating a string containing the original string and the string backwards.
def mirror(string):
    return string + string[::-1]
print(mirror('Pushpit'))

#Write a function that removes all occurences of a letter in a string.
def remove_letter(string,letter):
    for char in string:
        if char.lower() == letter or char.upper() == letter:
            string = string.replace(char,'')
    return string
print(remove_letter('Pushpit','p'))

#Implement python functions that works like the following list methods: count, in, reverse, index and insert.
def count(ele,lst):
    counter = 0
    for element in lst:
        if element == ele:
            counter+=1
    return counter
print(count('a',['a','p','p','l','e','b','a','n','a','n','a']))

def is_in(ele,lst):
    for element in lst:
        if element == ele:
            return True
    return False
print(is_in('i',['a','e','r','t']))

def reverse(lst):
    return lst[::-1]
print(reverse(['1','2','3','4','5']))

def index(ele,lst):
    for idx,element in enumerate(lst):
        if element == ele:
            return idx
print(index('p',['1','2','3','4','p','3',1,2,3]))

def insert(ele,pos,lst):
    new_list = []
    for i in range(len(lst)):
        if i == pos:
            new_list.append(ele)
        new_list.append(lst[i])
    return new_list
print(insert('cat',4,[1,2,3,4,6,7,8]))

#Write a function replace(s, old, new) that replaces all occurences of old with new in a string s
def replace(s,old,new):
    for char in s:
        if char == old:
            s = s.replace(char,new)
    return s
print(replace('Mississipi','i','I'))

#Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)
def maximum_value(lst):
    max = lst[0]
    for element in lst:
        if element > max:
            max = element
    return max
import random
random_no_list = []
for i in range(100):
    random_no_list.append(random.randint(0,1000))
print(maximum_value(random_no_list))

#Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs.
def sum_of_squares(xs):
    ss = 0
    for ele in xs:
        ss = ss + ele**2
    return ss
print(sum_of_squares([1,2,3,4,5,6,7,7,8]))

#Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.
#Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as: if abs(a-b) < 0.001:
def is_rightangled(a, b, c):
    return abs(a**2+b**2-c**2) < 0.001
print(is_rightangled(4.1,8.2,9.1678787077))

#You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6.
def divide(num):
    return num/2
def sum(num1):
    return divide(num1) + 6
print(sum(4))
