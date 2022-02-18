#Create a list called j_emotions that contains every word in emotion_words.txt that begins with the letter “j”.
j_emotions = list()
infile = open('emotion_words.txt','r')
for line in infile:
    words = line.strip().split()
    for word in words:
        if word[0]=='j':
            j_emotions.append(word)
infile.close()
print(j_emotions)
