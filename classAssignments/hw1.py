#Parker Bowling
#HW1
'''
BCPP 481
This is the first homework assignemnt
'''

def intsAndfloats():

    '''write your code below'''

    #declare an integer variable "myInt" and initialize it to a value of 10

    #declare a float variable "myFloat" and initalize it to a value of 15.2

    #add myInt and myFloat together and store it in a new variable called mySum

    #divide myFloat / myInt and store in a variable called myDivide

    #multiply myInt and myFloat and store in a variable called myMutiply

    #using myPower, take myInt to the power of myPower and store in a variable called result
    myPower = 3

    '''end of code'''

    '''uncomment this line when you are ready to submit'''
    #return (str(myInt) + " " + str(myFloat) + " " + str(mySum) + " " + str(myDivide) + " " + str(myMultiple) +  " " + str(result))

def stringFunction():

    '''write code below'''

    #declare a string called myString and initialize it to the value "Dr. Ring loves Python"
    
    #multiple this string by 2 and store in a variable called myString2

    #convert myInt to a string and store in a variable called convertedString
    myInt = 481

    #add String1 and String2 together, but add a space in between. Then store in a variable called combination
    String1 = "Dr. Ring"
    String2 = "loves Python"

    #add a newline character to myString and update the variable

    '''end of code'''

    '''uncomment this line when ready to submit'''
    #return (myString + myString2 + '\n' + str(type(convertedString)) + '\n' + combination)

def listsFunction():

    '''write code here'''

    #declare a list called myList with values of 25, 26, -1, 34, 7, 481, 31

    #get the length of the list and store it in a variable called myLength

    #get the first element of the list and store in a variable called firstIndex

    #append the number 300 to the end of the list

    #pop the third number off of the list

    #get the maximum and minimum value of myList and store in myMax and myMin, respectively

    #get the average of myList and store in myAverage, only use build in functions!

    '''end of code'''

    '''uncomment this line when ready to submit'''
    #return str(myList) + "\n" + str(myAverage)

def dictFunction():

    myDict = {
            "Gonzaga":"99",
            "TN Tech":"75",
            "Colorado":"66",
            "FGCU":"81",
            "Butler":"71"
            }

    '''write code here'''

    #get the TN Tech game score and store in a variable called game2

    #add the scores of the Colorado and Gonzaga scores and store in a variable called myGameScores

    #add the USC game score of 73 to the dictionary
    
    #use the keys() function to store the keys to the variable myKeys

    #use the values() function to store the values to the variable myValues

    #delete the Colorado game score from the dicitonary

    '''end of code'''

    '''uncomment this line when ready to submit'''
    #return (str(game2) + '\n' + str(twoGameScores) + "\n" + str(myKeys) + "\n" + str(myValues) + "\n" + str(myDict))

'''DO NOT TOUCH BELOW'''

print(intsAndfloats())
print(stringFunction())
print(listsFunction())
print(dictFunction())