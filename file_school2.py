#Using the file school_prompt.txt, assign the third word of every line to a list called three.
with open('school_prompt2.txt','r') as infile:
    three = list()
    for line in infile.readlines():
        words = line.strip().split()
        three.append(words[2])
print(three)
