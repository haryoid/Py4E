fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except FileNotFoundError:
    print(fname, 'not found!')
    exit()
count = dict()
for line in fhand:
    line = line.rstrip()
    word = line.split()
    #print(word)
    if len(word) == 0 or word[0] != 'From':
        continue
    if word[2] not in count:
        count[word[2]] = 1
    else:
        count[word[2]] += 1

print(count)
