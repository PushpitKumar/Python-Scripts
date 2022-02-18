#Get the user to enter some text and print it out in reverse order.
name = input('Enter any Name:')
reverse_name = ""
for char in name:
    reverse_name = char + reverse_name
print('Reversed Name:',reverse_name)
