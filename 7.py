file = input('enter a file name: ')
fhand = open(file)
#inp = fhand.read()
count = 0
for line in fhand:
    line = line.strip()
    if line.startswith('From:'):
        print(line)
#    count += 1
#fhand.close()


#print(count)
#print(inp[:10])
#mbox-short.txt