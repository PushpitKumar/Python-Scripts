#Create a list of numbers 0 through 40 and assign this list to the variable numbers. Then, accumulate the total of the list’s values and assign that sum to the variable sum1.
numbers = list(range(41))
sum1 = 0
for number in numbers:
    sum1 = sum1 + number
print('Sum of numbers from 0 to 40 is:',sum1)
