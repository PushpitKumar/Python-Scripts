#It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6). Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.
starting_day = int(input('Enter Your starting day of vacation:'))
duration = int(input('Enter Your duration of stay in days:'))
return_day = starting_day + duration
return_day = return_day%7
print('You will be back on:',return_day)
