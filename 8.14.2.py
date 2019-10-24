fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line.rstrip()
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        #print('Debug:', words)
        continue
    count += 1
    print(words[1])
#print('Debug2:', words)
#print(words[0])
print(count)