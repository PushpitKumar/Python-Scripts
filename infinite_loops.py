#So how can you recognize when you are in danger of making an infinite loop?
#First off, if the variable that you are using to determine if the while loop should continue is never reset inside the while loop, then your code will have an infinite loop. (Unless of course you use break to break out of the loop.)
#Additionally, if the while condition is while True: and there is no break, then that is another case of an infinite loop!Additionally, if the while condition is while True: and there is no break, then that is another case of an infinite loop!
while True:
    print('Will this stop?')
print('We have escaped!')

#Another case where an infinite loop is likely to occur is when you have reassiged the value of the variable used in the while statement in a way that prevents the loop from completing.
b = 15
while b < 60:
    b = 5
    print("Bugs")
    b = b + 7
#Notice how in this case, b is initally set to 15 outside of the while loop, and then reassigned the value of 5 inside, on line 3. By the time 7 has been added to b on line 5, we then have to check if b is less than 60. Because it isn’t we again run line 3, and set the value of b to 5 again. There is no way to break out of this loop.
#Sometimes programs can take a while to run, so how can you determine if your code is just talking a while or if it is stuck inside an infinite loop? Print statements are for people, so take advantage of them! You can add print statements to keep track of how your variables are changing as the program processes the instructions given to them.Sometimes programs can take a while to run, so how can you determine if your code is just talking a while or if it is stuck inside an infinite loop? Print statements are for people, so take advantage of them! You can add print statements to keep track of how your variables are changing as the program processes the instructions given to them.
