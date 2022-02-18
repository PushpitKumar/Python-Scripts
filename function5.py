def longer_than_five(lst_strings):
    for name in lst_strings:
        if len(name) > 5:
            return True
    return False

list1 = ["Sam","Tera","Sal","Amita"]
list2 = ["Rey","Ayo","Lauren","Natalie"]

print(longer_than_five(list1))
print(longer_than_five(list2))
