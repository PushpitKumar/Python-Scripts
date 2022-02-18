#addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val.
addition_str = "2+5+10+20"
addition_str = addition_str.split('+')
sum_val = 0
for val in addition_str:
    sum_val = sum_val + int(val)
print(sum_val)
