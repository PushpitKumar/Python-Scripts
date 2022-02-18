#Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
p_words = list()
with open('school_prompt2.txt','r') as infile:
    for line in infile:
        words = line.strip().split()
        for word in words:
            if 'p' in word:
                p_words.append(word)
print(p_words)
