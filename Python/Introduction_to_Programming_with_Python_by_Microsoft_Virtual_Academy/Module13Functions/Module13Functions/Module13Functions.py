#Define this function
#When someone calls this function, execute this code
def main() :
    names = getNames()    
    printNames(names)
    return

def getNames() :
    names = ['Eun', 'Koo', 'Kim']
    newName = input('Enter last guest : ')
    names.append(newName)
    return names

def printNames(names) :
    for name in names:
        message = getMessage(name)
        print(message)
    return

def getMessage(name) :
    return 'Hello, ' + name

#Execute the main function
#In order to do that the function must be created
main()
