#extract numbers from a given file. convert to integers and find the sum
import re

#established empty variable
sum = 0
#open the text file
file = open('data.txt')
#sift through lines and extract numbers
for line in file:
    x = re.findall('[0-9]+', line)
    #find the length of the returned list
    count = len(x)
    #while the lengnth of the list is NOT equal to 0, capture each string and convert to an interger. Add this together to find sum
    while count != 0:
        nums = int(x[(count - 1)])
        sum = sum + nums
        count -= 1

print(sum)
