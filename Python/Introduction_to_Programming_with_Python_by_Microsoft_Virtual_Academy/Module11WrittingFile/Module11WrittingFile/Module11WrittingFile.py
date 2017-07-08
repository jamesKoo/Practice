filename = 'demo.txt'
WRITE = 'w'
APPEND = 'a'

data = input('Please enter file info')

file = open(filename, mode = WRITE)
file.write(data)
file.close()

#file = open(filename, mode = WRITE)
#file.write('Susan, 29\n')
#file.write('Chirstopher, 31')
#file.write('This is the first line\n')
#file.write('This is the second line')
#file.close()

print('File written successfully')