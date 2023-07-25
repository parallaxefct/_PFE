#enter file name
name = input("Enter file:")
#default name
if len(name) < 1:
    name = "mbox-short.txt"
#file is opened in this varible
handle = open(name)
dates = {}

#this loop is built to isolate lines that start with 'From'
for line in handle:
    if line.startswith('From '):
        str = line.split()

        #this loop is built to isolate the dates
        for line in str:
            if ':' in line:
                num = line.split(':')
                dates[num[0]] = dates.get(num[0], 0) + 1

#this loop returns key/value pairs to then output
for k,v in sorted(dates.items()):
    print(k,v)
