import random

from importedfile import add    
import matplotlib.pyplot as plt

num1 = 5
num2 = 19

myList = []

allNumber = []

for i in range(10):
    x = random.randint(0,100)
    myList.append(x)
    allNumber.append(i)

myList[4] = 5

index5 = myList[4]

# if (condition):
#   execute
# else: 
# execute else

if index5 % 2 != 0:
    print("is even")    

#if index5 % 3 == 0:
 #   print("divisible by 3")


#this is even
#this is odd

print(myList)



