#For each word in the list verbs, add an -ing ending. Overwrite the old list so that verbs has the same words with ing at the end of each one.

verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
for verb in range(len(verbs)):
    verbs[verb] = verbs[verb] + 'ing'
print(verbs)

#Another method is to use enum.
verbs2 = ["kayak", "cry", "walk", "eat", "drink", "fly"]
for idx,item in enumerate(verbs2):
    verbs2[idx] = verbs2[idx] + 'ing'
print(verbs2)
