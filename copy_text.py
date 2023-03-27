#prompt for input of file name
#open the file and read through
#print content of file in upper case

fname = input('Enter file name: ')
file = open(fname)
str = file.read()

capStr = str.upper()

print(capStr)
