file = open('olympics.txt','r')
for line in file.readlines()[1:]: #skip the first line since it is the header
    values = line.split(',')
    print(values[0],'is from',values[3],'and is on the roster for',values[4])
file.close()

#the below technique simplifies the process of iterating through contents of a file one line at a time, without first reading them into a list.
file = open('olympics.txt','r')
for line in file:
    values = line.split(',')
    print(values[0],'is from',values[3],'and is on the roster for',values[4])
file.close()

#Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
file = open('emotion_words.txt','r')
num_lines = 0
for line in file.readlines():
    num_lines+=1
print(num_lines)
