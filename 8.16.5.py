finp = input('Enter a file name: ')
fopen = open(finp)
count = 0
tfrom = []
for line in fopen:
    line.rstrip()
    word = line.split()
    #print(word)
    if len(word) == 0:  continue
    if word[0] != 'From':   continue
    if word[1] not in tfrom:
        tfrom.append(word[1])
    count += 1
    #print(word[1])
print('there where', count, 'lines in the file with From as the first word')
print('this is list of', len(tfrom), 'sender\n', tfrom)

