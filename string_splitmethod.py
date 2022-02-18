#Split method breaks the string into a list of words. Whitespace is used for splitting by default.
song = 'The rain in Spain...'
words = song.split()
print(words)

#An optional arguement called delimiter can be used for splitting the string.
x = 'leaders and best'
words = x.split('e')
print(words)

song2 = 'The rain in Spain'
wds = song2.split('ai')
print(wds)
