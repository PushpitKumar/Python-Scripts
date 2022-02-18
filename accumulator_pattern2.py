# Write a program to add first n odd numbers
n = int(input('How many first n odd numbers do you want to add?'))
sum_odd_num = 0
odd_num = 1
for _ in range(n):
    sum_odd_num = sum_odd_num + odd_num
    odd_num = odd_num + 2
print('Sum of first',n,'odd numbers:',sum_odd_num)
