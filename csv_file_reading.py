file = open('olympics.txt','r')
lines = file.readlines()
header = lines[0]
field_names = header.strip().split(',')
for line in lines[1:]:
    vals = line.strip().split(',')
    if vals[5]!='NA':
        print('{}: {}: {}'.format(
        vals[0],
        vals[4],
        vals[5]
        ))
file.close()
