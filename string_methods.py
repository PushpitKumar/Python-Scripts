ss = 'Hello, World!'
print(ss.upper()) #creates a new string with uppercase letters

tt = ss.lower() #creates a new string with lowercase letters
print(tt)
print(ss) #original string remains unchanged

ss = '   Hello, World    '
els = ss.count('l') #returns the number of occurences of item #
print(els)

print('***'+ss.strip()+'***') #removes trailing and leading whitespace. original string is not modified

news = ss.replace('o','***') #replaces all occurences of first arguement with the second arguement in the string
print(news)
