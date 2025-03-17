#read first line of file
file = open('file.txt', 'r')
print("Reading first line... ")
print(file.radline())
file.close()


# read first three lines of file
file = open('file.txt', 'r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#looping through all the lines of the file
file = open('Codingal.txt', 'r')
print("looping through the lines....")
for line in file:
    print(line)
    file.close()
