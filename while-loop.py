def sumTo(abound):
    """ Return the sum of 1+2+3 ... n """
    theSum = 0
    anumber = 1
    while anumber <= abound:
        theSum = theSum + anumber
        anumber+=1
    return theSum
print(sumTo(4))
print(sumTo(1000))

#You can almost read the while statement as if it were in natural language. It means, while aNumber is less than or equal to aBound, continue executing the body of the loop. Within the body, each time, update theSum using the accumulator pattern and increment aNumber. After the body of the loop, we go back up to the condition of the while and reevaluate it. When aNumber becomes greater than aBound, the condition fails and flow of control continues to the return statement.
#More formally, here is the flow of execution for a while statement:
#1. Evaluate the condition, yielding False or True.
#2. If the condition is False, exit the while statement and continue execution at the next statement.
#3. If the condition is True, execute each of the statements in the body and then go back to step 1.
#This type of flow is called a loop because the third step loops back around to the top. Notice that if the condition is False the first time through the loop, the statements inside the loop are never executed.
#The body of the loop should change the value of one or more variables so that eventually the condition becomes False and the loop terminates. Otherwise the loop will repeat forever. This is called an infinite loop. An endless source of amusement for computer scientists is the observation that the directions written on the back of the shampoo bottle (lather, rinse, repeat) create an infinite loop.
#Introduction of the while statement causes us to think about the types of iteration we have seen. The for statement will always iterate through a sequence of values like the list of names for the party or the list of numbers created by range. Since we know that it will iterate once for each value in the collection, it is often said that a for loop creates a definite iteration because we definitely know how many times we are going to iterate. On the other hand, the while statement is dependent on a condition that needs to evaluate to False in order for the loop to terminate. Since we do not necessarily know when this will happen, it creates what we call indefinite iteration. Indefinite iteration simply means that we don’t know how many times we will repeat but eventually the condition controlling the iteration will fail and the iteration will stop. (Unless we have an infinite loop which is of course a problem)
#What you will notice here is that the while loop is more work for you — the programmer — than the equivalent for loop. When using a while loop you have to control the loop variable yourself. You give it an initial value, test for completion, and then make sure you change something in the body so that the loop terminates. That also makes a while loop harder to read and understand than the equivalent for loop. So, while you can implement definite iteration with a while loop, it’s not a good idea to do that. Use a for loop whenever it will be known at the beginning of the iteration process how many times the block of code needs to be executed.

#Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
i = 0
eve_nums = []
while i <= 15:
    if i%2 == 0:
        eve_nums.append(i)
    i+=1
print(eve_nums)

#Write a code to sum up all the elements of given list using while loop. Assign the accumulator variable to the name accum.
list1 = [8,3,4,5,6,7,9]
accum = 0
i = 0
while i < len(list1):
    accum = accum + list1[i]
    i+=1
print(accum)

#Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.
def stop_at_four(lst):
    new_list = []
    i = 0
    while i < len(lst):
        if lst[i] == 4:
            return new_list
        new_list.append(lst[i])
        i+=1
print(stop_at_four([1,2,3,5,6,7,8,4,9,10]))
