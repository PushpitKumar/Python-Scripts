#You can also use a while loop when you want to validate input; when you want to make sure the user has entered valid input for a prompt. Let’s say you want a function that asks a yes-or-no question. In this case, you want to make sure that the person using your program enters either a Y for yes or N for no (in either upper or lower case). Here is a program that uses a while loop to keep asking until it receives a valid answer. As a preview of coming attractions, it uses the upper() method which is described in String Methods to convert a string to upper case. 
def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print("Please enter 'Y' for Yes or 'N' for No")
    return answer
response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')
if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')
