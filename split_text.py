import mbox_short

fname = mbox_short.mboxShort

#if len(fname) < 1:
#    fname = "mbox-short.txt"

#fh = open(fname)
count = 0

for line in fname:
    if line.startswith("From"): ###this line needs to be fixed
        words = line.split()
        print(words[2])
        count += 1

    else:
        continue

print(f"There were", {count}, "lines in the file with From as the first word")
