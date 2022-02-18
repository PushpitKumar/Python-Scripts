#Mutating methods are ones that change the object after the method has been used. Non-mutating methods do not change the object after the method has been used.
#The count and index methods are both non-mutating. Count returns the number of occurances of the argument given but does not change the original string or list. Similarly, index returns the leftmost occurance of the argument but does not change the original string or list.

mylist = []
mylist.append(80) #mutator, adds new item to the end of the list
mylist.append(90)
mylist.append(100)
mylist.append(200)
mylist.append(110)
mylist.append(55)
mylist.append(70)
print(mylist)

mylist.insert(1,12) #Insert 12 at index 1. mutator, inserts a new item at a given position
print(mylist)

print(mylist.count(12)) #counts the number of occurence of arguement in the list. non-mutator

print(mylist.index(200)) #returns the first occurence of item. non-mutator

mylist.reverse() #mutator, modifies list to be in reverse order
print(mylist)

mylist.sort() #mutator, modifies list to be sorted in ascending order
print(mylist)

mylist.remove(55) #mutator,removes the first occurence of item

last_item = mylist.pop() #hybrid, removes and returns the last item or index specified in the argument.
print(last_item)
print(mylist)

#It is important to remember that methods like append, sort, and reverse all return None. They change the list; they don’t produce a new list.
