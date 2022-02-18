#Sorting a dictionary
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x not in d:
        d[x] = 0
    d[x] = d[x] + 1
y = sorted(d.keys())

for k in y:
    print('{} appears {} times'.format(k,d[k]))
print('\n')
#With a dictionary that’s maintaining counts or some other kind of score, we might prefer to get the outputs sorted based on the count rather than based on the items. The standard way to do that in python is to sort based on a property of the key, in particular its value in the dictionary.
#Here things get a little confusing because we have two different meaning of the word “key”. One meaning is a key in a dictionary. The other meaning is the parameter name for the function that you pass into the sorted function.
#Remember that the key function always takes as input one item from the sequence and returns a property of the item. In our case, the items to be sorted are the dictionary’s keys, so each item is one key from the dictionary. To remind ourselves of that, we’ve named the parameter in tha lambda expression k. The property of key k that is supposed to be returned is its associated value in the dictionary. Hence, we have the lambda expression lambda k: d[k].

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

dictionary = {}
for char in L:
    if char not in dictionary:
        dictionary[char] = 0
    dictionary[char] = dictionary[char] + 1
y = sorted(d.keys(),reverse=True,key=lambda k:dictionary[k])
for k in y:
    print('{} appears {} times'.format(k,dictionary[k]))
print('\n')
#When we sort the keys, passing a function with key=lambda x: d[x] does not specify to sort the keys of a dictionary. The lists of keys are passed as the first parameter value in the invocation of sort. The key parameter provides a function that says how to sort them.

#Here’s a version of that using a named function.

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k):
    return d[k]

y =(sorted(d.keys(), key=g, reverse=True))
for k in y:
    print("{} appears {} times".format(k, d[k]))
print('\n')
#An experienced programmer would probably not even separate out the sorting step. And they might take advantage of the fact that when you pass a dictionary to something that is expecting a list, its the same as passing the list of keys.
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:

    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

# now loop through the sorted keys
for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))
print('\n')
#There is another way to sort dictionaries, by calling .items() to extract a sequence of (key, value) tuples, and then sorting that sequence of tuples. But it’s better to learn the pythonic way of doing it, sorting the dictionary keys using a key function that takes one key as input and looks up the value in the dictionary.

#Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable sorted_keys.Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable sorted_keys.
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_keys = sorted(dictionary)
print(sorted_keys)
print('\n')

#Sort the following dictionary’s keys based on the value from highest to lowest. Assign the resulting value to the variable sorted_values.
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values = sorted(dictionary.keys(),reverse=True,key=lambda k:dictionary[k])
print(sorted_values)
