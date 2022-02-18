text = input('Enter any text:')
reverse_text = ""
for char in text:
    reverse_text = char+reverse_text
print('Reversed text:',reverse_text)
if text == reverse_text:
    print('This is a palindrome!')
else:
    print('This is not a palindrome!')
