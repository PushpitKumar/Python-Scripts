text = input('Enter any text:')
print('Reversed text:',text[::-1])
if text[:] == text[::-1]:
    print('This is a palindrome!')
else:
    print('This is not a palindrome!')
