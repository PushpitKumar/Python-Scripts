#The typical pattern for writing data to a CSV file will be to write a header row and loop through the items in a list, outputting one row for each. Here we a have a list of tuples, each representing one Olympian, a subset of the rows and columns from the file we have been reading from.
olympians = [("John Aalberg",31,"Country Skiing"),
             ("Minna Maarit Aalto",30,"Sailing"),
             ("Wakako Abe",30,"Cycling")]
outfile = open("reduced_olympics.csv","w")
#Output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
#output each of the rows
for olympian in olympians:
    row_string = '"{}","{}","{}"'.format(olympian[0],olympian[1],olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()
