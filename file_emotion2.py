#Find the total number of words in the file emotion_words.txt and assign this value to the variable num_words.
infile = open('emotion_words.txt','r')
num_words = 0
for line in infile:
    words = line.strip().split()
    num_words = num_words + len(words)
infile.close()
print(num_words)
