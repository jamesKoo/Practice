import csv

#Open my file
with open('Tasmania.txt', 'r') as animalFile:
    allRowsList = csv.reader(animalFile)

    for currentRow in allRowsList :
        print(','.join(currentRow))

        #for data in currentRow :
        #    print(data)

#Read file line by line
#firstAnimal = animalFile.readline()
#print(firstAnimal)
#secondAnimal = animalFile.readline()
#print(secondAnimal)

#Read all file contents
#allFilecontents = animalFile.read()
#print(allFilecontents);