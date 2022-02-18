#Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.
pirate = dict()
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['madam'] = 'proud beauty'
pirate['professor'] = 'foul blaggart'
pirate['restaurant'] = 'galley'
pirate['your'] = 'yer'
pirate['excuse'] = 'arr'
pirate['students'] = 'swabbies'
pirate['are'] = 'be'
pirate['lawyer'] = 'foul blaggart'
pirate['the'] = "th'"
pirate['restroom'] = 'head'
pirate['my'] = 'me'
pirate['hello'] = 'avast'
pirate['is'] = 'be'
pirate['man'] = 'matey'
e_sentence = input('Enter any sentence in English:')
p_sentence = list()
words = e_sentence.split()
for word in words:
    if word in pirate:
        p_sentence.append(pirate[word])
    else:
        p_sentence.append(word)
print('Sentence translated in Pirate:'," ".join(p_sentence))    
