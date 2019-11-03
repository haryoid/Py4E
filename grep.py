import re

inp = input('Enter a regular exspresion: ')
fopen = open('mbox.txt')

count = 0
for line in fopen:
    line = line.rstrip()
    if re.search(inp, line):
        count += 1

print(inp, count)