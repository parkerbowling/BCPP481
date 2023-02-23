from random import randrange

#Parker Bowling
#HW2
#BCPP481
#This is the second homework

#constants, do not touch
myList = [23, 2135, 15 ,15, 16 ,621, 46, 134, -134, 35, 135, 53, 9753, 356, 63568, 86, 34, 638, 863,]


def conditionals1():

    #get the 9th element of the list and
    # write an if/else statement that assigns
    # a boolean value to the variable x
    # if the number is an even number
    x = None

    '''code goes here'''

    '''end of code'''

    #uncomment when ready to submit
    #return str(x)

def conditionals2():

    #this chooses a random number from 1 to 3
    randInt = randrange(1,4)  

    #write a condition that
    # if randInt equals 1 then print "Hello World" to the screen
    # else if randInt equals 2 then print "This is the second option" to the screen
    # else if randInt equals 3 then print "Dr. Ring loves python" to the screen"
    
    '''code goes here'''

    '''end of code'''

    #uncomment when ready to submit
    #return str(randInt)
  
def stringSlicing1():

    myString = "Life is either a daring adventure or nothing at all."

    "write code here"

    #print the length of myString

    #print the first word of the quote

    #print all the words but the first and last word 
    # (make sure there are no spaces at either end of your slice)

    #print the string backwards

    #print the last word (including the period) backwards

    '''end of code'''


print(conditionals1())
print(conditionals2())
stringSlicing1()