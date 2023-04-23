#extract numbers from a given file. convert to integers and find the sum
import re

file = open('data.rtf')

for line in file:
    nums = re.findall('[0-9]+', line)
    print(nums)
