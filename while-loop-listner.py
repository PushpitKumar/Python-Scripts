#Usually, in python, you will use a for loop rather than a while loop. When is it not known at the beginning of the iteration how many times the code block needs to be executed? The answer is, when it depends on something that happens during the execution.
#One very common pattern is called a listener loop. Inside the while loop there is a function call to get user input. The loop repeats indefinitely, until a particular input is received.
sum = 0
x = -1
while x!= 0:
    x = int(input('Next number to add up (Enter 0 if no more numbers):'))
    sum = sum + x
print(sum)
#This is just our old friend, the accumulation pattern, adding each additional output to the sum-so-far, which is stored in a variable called theSum and reassigned to that variable on each iteration. Notice that theSum is initialized to 0. Also notice that we had to initialize x, our variable that stores each input that the user types, before the while loop. This is typical with while loops, and makes them a little tricky to read and write. We had to initialize it because the condition x != 0 is checked at the very beginning, before the code block is ever executed. In this case, we picked an initial value that we knew would make the condition true, to ensure that the while loop’s code block would execute at least once.

#Indefinite loops are much more common in the real world than definite loops.
#1. If you are selling tickets to an event, you don’t know in advance how many tickets you will sell. You keep selling tickets as long as people come to the door and there’s room in the hall.
#2. When the baggage crew unloads a plane, they don’t know in advance how many suitcases there are. They just keep unloading while there are bags left in the cargo hold. (Why your suitcase is always the last one is an entirely different problem.)
#3. When you go through the checkout line at the grocery, the clerks don’t know in advance how many items there are. They just keep ringing up items as long as there are more on the conveyor belt.

#Let’s implement the last of these in Python, by asking the user for prices and keeping a running total and count of items. When the last item is entered, the program gives the grand total, number of items, and average price.
def checkout():
    total = 0
    count = 0
    moreitems = True
    while moreitems:
        price = float(input('Enter price of item (0 when done):'))
        if price!=0: #Here 0 is known as the sentinel value. A value used to signal the end of the loop.
            total = total + price
            count+=1
            print('Subtotal: $',total)
        else:
            moreitems = False
    avg = total/count
    print('Total Items:',count)
    print('Total: $',total)
    print('Average price per item: $',avg)
checkout()

#There are still a few problems with this program.
#1. If you enter a negative number, it will be added to the total and count. Modify the code so that negative numbers give an error message instead (but don’t end the loop)
#2. If you enter zero the first time you are asked for a price, the loop will end, and the program will try to divide by zero.
#3. This program doesn’t display the amounts to two decimal places.

def checkout1():
    total = 0
    count = 0
    moreitems = True

    while moreitems:
        price = float(input('Enter price of item (o when done):'))
        if price!=0 and price>0:
            total = total + price
            count+=1
            print('Subtotal: $',total)
        elif price<0:
            continue
        else:
            moreitems = False
    if total == 0:
        print('You need by at least 1 item to compute the average total')
    else:
        avg = total/count
        print('Total Items:',count)
        print('Total: $',total)
        print('Average price per item: $',avg)
checkout1()
