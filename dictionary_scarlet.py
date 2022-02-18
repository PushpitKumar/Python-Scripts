#Write a program that finds the most used 7 letter word in scarlet3.txt.
with open('scarlet3.txt','r') as infile:
    d = {}
    for line in infile:
        words = line.strip().split()
        for word in words:
            if len(word)==7:
                if word not in d:
                    d[word] = 0
                d[word] = d[word] + 1
    keys = list(d.keys())
    most_used_7_letter_word_so_far = keys[0]
    for key in keys:
        if d[key] > d[most_used_7_letter_word_so_far]:
            most_used_7_letter_word_so_far = key
    print(most_used_7_letter_word_so_far,'is the most used 7 letter word, appearing a total of:',d[most_used_7_letter_word_so_far],'times')

            
