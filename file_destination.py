#Create a list called destination using the data stored in travel_plans.txt. Each element of the list should contain a line from the file that lists a country and cities inside that country.
destination = list()
infile = open('travel_plans2.txt','r')
for line in infile:
    if ':' in line:
        destination.append(line)
infile.close()
print(destination)
