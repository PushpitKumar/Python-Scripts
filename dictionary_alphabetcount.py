#Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored.
sentence = input('Enter any sentence:')
lowered = sentence.lower()
d = {}
for char in lowered:
    if char not in d:
        d[char] = 0
    d[char] = d[char] + 1
for key in sorted(d.keys()):
    print(key,d[key])
