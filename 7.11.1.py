# Python to open file and print per line in Uppercase
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.upper()
    print(line)