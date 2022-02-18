#Write code that asks the user to enter a numeric score (0-100). In response, it should print out the score and corresponding letter grade, according to the table below.
#>=90 A; [80-90) B; [70-80) C; [60-70) D; <60 F. The square and round brackets denote closed and open intervals. A closed interval includes the number, and open interval excludes it. So 79.99999 gets grade C , but 80 gets grade B.
score = float(input('Enter score between 0-100:'))
if score >=90:
    grade = 'A'
    print('Your Score is:',score,'and Grade is:',grade)
elif score >=80 and score <90:
    grade = 'B'
    print('Your Score is:',score,'and Grade is:',grade)
elif score >=70 and score <80:
    grade = 'C'
    print('Your Score is:',score,'and Grade is:',grade)
elif score >=60 and score <70:
    grade = 'D'
    print('Your Score is:',score,'and Grade is:',grade)
else:
    grade = 'F'
    print('Your Score is:',score,'and Grade is:',grade)
