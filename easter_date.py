year = int(input('Enter any year between 1900-2099:'))
if year>1900 and year<2099:
    a = year%19
    b = year%4
    c = year%7
    d = (19*a+24)%30
    e = (2*b+4*c+6*d+5)%7
    date_of_easter = 22+d+e
    if year in [1954,1981,2049,2076]:
        date_of_easter = date_of_easter - 7
else:
    print('Year is out range!')
if date_of_easter>31:
    print('Date of Easter Sunday:',date_of_easter-31,'->April')
else:
    print('Date of Easter Sunday:',date_of_easter,'->March')
