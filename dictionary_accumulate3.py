#suppose that we wanted to compute a Scrabble score for the Study in Scarlet text. Each occurrence of the letter ‘e’ earns one point, but ‘q’ earns 10. We have a second dictionary, stored in the variable letter_values. Now, to compute the total score, we start an accumulator at 0 and go through each of the letters in the counts dictionary. For each of those letters that has a letter value (no points for spaces, punctuation, capital letters, etc.), we add to the total score.
with open('scarlet2.txt','r') as infile:
    txt = infile.read()
    letters = {}
    for char in txt:
        if char not in letters:
            letters[char] = 0
        letters[char] = letters[char] + 1
    letter_values = {'a':1,'b':2,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}
    tot = 0
    for letter in letters:
        if letter in letter_values:
            tot = tot + letters[letter] * letter_values[letter] # We are updating the variable tot to have its old number plus the score for the current letter times the number of occurrences of that letter.
print(tot)
