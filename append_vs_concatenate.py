# consider we have a list called origlist. We want to add the word 'cat' to the end of the list.
origlist = [45,32,88]
origlist.append('cat')#Here we have used append which simply modifies the list.
#In order to use concatenation, we need to write an assignment statement that uses the accumulator pattern.
origlist = [45,32,88]
new_list = origlist + ['cat'] #origlist remains unchanged
#It is also important to realize that with append, the original list is simply modified. On the other hand, with concatenation, an entirely new list is created.

#In Python, every object has a unique identification tag. Likewise, there is a built-in function that can be called on any object to return its unique id. The function is appropriately called id and takes a single parameter, the object that you are interested in knowing about.
origlist = [45,32,88]
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list before changes
newlist = origlist + ['cat']
print("newlist:", newlist)
print("the identifier:", id(newlist))              #id of the list after concatentation
origlist.append('cat')
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list after append is used

#Note how even though newlist and origlist appear the same, they have different identifiers.

#We have previously described x += 1 as a shorthand for x = x + 1. With lists, += is actually a little different. In particular, origlist += [“cat”] appends “cat” to the end of the original list object. If there is another alias for `origlist, this can make a difference
origlist = [45,32,88]
aliaslist = origlist
origlist += ["cat"] #modifies the existing origlist
origlist = origlist + ["cow"] #creates a newlist object
