#The write method allows us to add data to a text file. Recall that text files contain sequences of characters. We usually think of these character sequences as being the lines of the file where each line ends with the newline \n character. Be very careful to notice that the write method takes one parameter, a string. When invoked, the characters of the string will be added to the end of the file. This means that it is the programmer’s job to include the newline characters as part of the string if desired.
filename = 'squared_numbers.txt'
outfile = open(filename,'w')

for number in range(1,13):
    squared = number**2
    outfile.write(str(squared)+'\n')

outfile.close()

infile = open(filename,'r')
for line in infile:
    print(line)
infile.close()
