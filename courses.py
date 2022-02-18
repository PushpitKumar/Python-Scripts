#In XYZ University, upper level math classes are numbered 300 and up. Upper level English classes are numbered 200 and up. Upper level Psychology classes are 400 and up. Create two lists, upper and lower. Assign each course in classes to the correct list, upper or lower.
classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
upper = list()
lower = list()
for sub in classes:
    if sub in ['MATH 300','MATH 404','ENG 201','ENG 220','PSYCH 412','PSYCH 508']: #There's some case of hard-coding here
        upper.append(sub)
    else:
        lower.append(sub)
print(upper)
print(lower)

#A better generalised code is given below.

classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
upper2 = list()
lower2 = list()
for course in classes:
    space = course.find(' ')
    num = course[space:]
    if int(num) >= 300 and course[:space] == 'MATH':
        upper2.append(course)
    elif int(num) >= 200 and course[:space] == 'ENG':
        upper2.append(course)
    elif int(num) >= 400 and course[:space] == 'PSYCH':
        upper2.append(course)
    else:
        lower2.append(course)
print(upper2)
print(lower2)
