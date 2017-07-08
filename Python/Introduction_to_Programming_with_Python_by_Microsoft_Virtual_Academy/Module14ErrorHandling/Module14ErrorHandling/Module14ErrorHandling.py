import sys

firstNumber = float(input("enter a number "))
secondNumber = float(input("enter a number "))

try :
    result = firstNumber / secondNumber
    print(result)
except ZeroDivisionError :
    print("The answer is infinity.")
    #error = sys.exc_info()[0]
    #print(error)
    #print("I am sorry someting went wrong.")
finally :
    print("I will always run.")