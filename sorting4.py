#Breaking ties: Second sorting
#What happens when two items are “tied” in the sort order? For example, suppose we sort a list of words by their lengths. Which five letter word will appear first?
#The answer is that the python interpreter will sort the tied items in the same order they were in before the sorting.
#What if we wanted to sort them by some other property, say alphabetically, when the words were the same length? Python allows us to specify multiple conditions when we perform a sort by returning a tuple from a key function.
#First, let’s see how python sorts tuples. We’ve already seen that there’s a built-in sort order, if we don’t specify any key function. For numbers, it’s lowest to highest. For strings, it’s alphabetic order. For a sequence of tuples, the default sort order is based on the default sort order for the first elements of the tuples, with ties being broken by the second elements, and then third elements if necessary, etc. For example,
tups = [('A',3,2),
        ('C',1,4),
        ('B',3,1),
        ('A',2,4),
        ('C',1,2)]
for tup in sorted(tups):
    print(tup)

#In the code below, we are going to sort a list of fruit words first by their length, smallest to largest, and then alphabetically to break ties among words of the same length. To do that, we have the key function return a tuple whose first element is the length of the fruit’s name, and second element is the fruit name itself.
fruits = ['peach','kiwi','apple','blueberry','papaya','mango','pear']
new_order = sorted(fruits,key=lambda fruit_name: (len(fruit_name),fruit_name))
print(new_order)

#Here, each word is evaluated first on it’s length, then by its alphabetical order. Note that we could continue to specify other conditions by including more elements in the tuple.
#What would happen though if we wanted to sort it by largest to smallest, and then by alphabetical order?
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)
print(new_order)

#Do you see a problem here? Not only does it sort the words from largest to smallest, but also in reverse alphabetical order!
#One solution is to add a negative sign in front of len(fruit_name), which will convert all positive numbers to negative, and all negative numbers to positive. As a result, the longest elements would be first and the shortest elements would be last.
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
print(new_order)

weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))
print(sorted_weather)

weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, -weather[w]['temp']), reverse=True)
print(sorted_weather)
