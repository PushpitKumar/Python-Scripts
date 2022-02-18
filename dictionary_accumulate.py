#We can accumulate counts for more than one character as we traverse the text. Suppose, for example, we wanted to compare the counts of ‘t’ and ‘s’ in the text.
with open('scarlet.txt','r') as infile:
    txt = infile.read() ## now txt is one long string containing all the characters
    tcount = 0
    scount = 0
    for char in txt:
        if char=='t':
            tcount+=1
        elif char=='s':
            scount+=1
print('s:',str(scount),'occurences')
print('t:',str(tcount),'occurences')

#OK, but you can see this is going to get tedious if we try to accumulate counts for all the letters. We will have to initialize a lot of accumulators, and there will be a very long if..elif..elif statement. Using a dictionary, we can do a lot better.
#One dictionary can hold all of the accumulator variables. Each key in the dictionary will be one letter, and the corresponding value will be the count so far of how many times that letter has occurred.
with open('scarlet.txt','r') as infile:
    txt = infile.read()
    x = {} #start with an empty dictionary
    x['t'] = 0 #initialize the t counter
    x['s'] = 0 #initialize the s counter
    for char in txt:
        if char=='t':
            x['t'] = x['t'] + 1 #increment the t counter
        elif char=='s':
            x['s'] = x['s'] + 1 #increment the s counter
print('s:',str(x['s']),'occurences')
print('t:',str(x['t']),'occurences')

#But this hasn;t really improved our code. Incrementing the counter for each character can be done by just incrementing the loop variable as shown below
with open('scarlet.txt','r') as infile:
    txt = infile.read()
    x = {}
    x['t'] = 0
    x['s'] = 0
    for char in txt:
        if char=='t':
            x[char] = x[char] + 1
        elif char=='s':
            x[char] = x[char] + 1
print('s:',str(x['s']),'occurences')
print('t:',str(x['t']),'occurences')

#We can do better still. One other nice thing about using a dictionary is that we don’t have to prespecify what all the letters will be. In this case, we know in advance what the alphabet for English is and we do not know in advance all the of the words that may be used. Rather than pre-specifying which letters to keep accumulator counts for, we can start with an empty dictionary and add a counter to the dictionary each time we encounter a new thing that we want to start keeping count of.
with open('scarelt.txt','r') as infile:
    txt = infile.read()
    x = {}
    for char in txt:
        if char not in x:
            x[char] = 0 #we have not seen this character before, so initialize a counter for it
        x[char] = x[char] + 1#whether we've seen it before or not, increment its counter
print('s:',str(x['s']),'occurences')
print('t:',str(x['t']),'occurences')

#Notice that in the for loop, we no longer need to explicitly ask whether the current letter is an ‘s’ or ‘t’. The increment step on line 11 works for the counter associated with whatever the current character is. Our code is now accumulating counts for all letters, not just ‘s’ and ‘t’.
#Note that the print statements at the end pick out the specific keys ‘t’ and ‘s’. We can generalize that, too, to print out the occurrence counts for all of the characters, using a for loop to iterate through the keys in x.
with open('scarlet.txt','r') as infile:
    txt = infile.read()
    letter_counts = {}
    for char in txt:
        if char not in letter_counts:
            letter_counts[char] = 0
        letter_counts[char] = letter_counts[char] + 1
for c in letter_counts.keys():
    print(c,':',str(letter_counts[c]),'occurences')

#Note that only those letters that actually occur in the text are shown. Some punctuation marks that are possible in English, but were never used in the text, are omitted completely. The blank line partway through the output may surprise you. That’s actually saying that the newline character, \\n, appears 5155 times in the text. In other words, there are 5155 lines of text in the file. Let’s test that hypothesis.
with open('scarlet.txt','r') as infile:
    lines = infile.readlines()
print(len(lines))
