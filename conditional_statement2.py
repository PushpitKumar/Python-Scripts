#Create an empty list called resps. Using the list percent_rain, for each percent, if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps.
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = list()
for rain in percent_rain:
    if rain > 90:
        resps.append('Bring an umbrella.')
    elif rain > 80:
        resps.append('Good for the flowers?')
    elif rain > 50:
        resps.append('Watch out for clouds!')
    else:
        resps.append('Nice day!')
print(resps)
