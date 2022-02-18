#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
infile = open('travel_plans2.txt','r')
chars = infile.read()
num = len(chars)
infile.close()
print(num)
