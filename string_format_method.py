person = input('Enter your name:')
print('Hello {}'.format(person))

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage:'))
newPrice = (1-discount/100)*origPrice
calculation = '${} discounted by {}% is ${}'.format(origPrice,discount,newPrice)
print(calculation)
#It is important to pass arguments to the format method in the correct order, because they are matched positionally into the {} places for interpolation where there is more than one.
#Format strings can give further information inside the braces showing how to specially format data. In particular floats can be shown with a specific number of decimal places. For two decimal places, put :.2f inside the braces for the monetary values.
calculation = '${:.2f} discounted by {}% is ${:.2f}'.format(origPrice,discount,newPrice) #The 2 in the format modifier can be replaced by another integer to round to that specified number of digits.
print(calculation)

v = 2.34567
print('{:.1f} {:.2f} {:.7f}'.format(v, v, v))

#A technical point: Since braces have special meaning in a format string, there must be a special rule if you want braces to actually be included in the final formatted string. The rule is to double the braces: \{\{ and \}\}. For example mathematical set notation uses braces. The initial and final doubled braces in the format string below generate literal braces in the formatted string:
