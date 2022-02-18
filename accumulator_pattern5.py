#week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp..
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f = week_temps_f.split(',')
sum_temp = 0
for temp in week_temps_f:
    sum_temp = sum_temp + float(temp)
avg_temp = sum_temp/len(week_temps_f)
print(avg_temp)
