#This method is the inverse of split. You choose a desired seperator string often called (Glue) and join the list of strings with the gluje between each of the elements.
words = ['leaders','and','best']
glue = '/'
s = glue.join(words)
print(s)
print(words) #original list doesn't change

words2 = ['red','blue','green']
glue2 = ';'
x = glue2.join(words2)
print(x)
print('***'.join(words2))
print("".join(words2))
