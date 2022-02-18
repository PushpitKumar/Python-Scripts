#You’re going to write a function that takes a string as a parameter and returns a list of the five most frequent characters in the string.
def five_most_frequent_characters(string):
    d = dict()
    for char in string:
        if char not in d:
            d[char] = 0
        d[char] = d[char] + 1
    sorted_characters = sorted(d,key=lambda char: d[char],reverse=True)
    return sorted_characters[:5]
print(five_most_frequent_characters('A Game of Thrones'))

#Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters,reverse=True)
print(('').join(sorted_letters))

#Write code to rearrange the strings in the list winners so that they are in alphabetical order by first name from A to Z
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()
print(winners)

#Write code to switch the order of the winners list so that it is now Z to A, by first name. Assign this list to the variable z_winners.
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners = sorted(winners,reverse=True)
print(z_winners)

#Write code to switch the order of the winners list so that it is now A to Z by last name. Assign this list to the variable z_winners.
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners = sorted(winners,key=lambda name: name.split()[-1])
print(z_winners)

#The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)

#Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
sorted_medals = sorted(medals, key=lambda k: medals[k],reverse=True)
top_three = sorted_medals[:3]
print(top_three)

#We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries,key=lambda k: groceries[k],reverse=True)
print(most_needed)

#Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids.
def last_four(x):
    str_x = str(x)
    return str_x[-4]
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids,key=last_four)
print(sorted_ids)

#Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids,key=lambda id: str(id)[-4:])
print(sorted_id)

#Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst,key=lambda i: i[1])
print(lambda_sort)
