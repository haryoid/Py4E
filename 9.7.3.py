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
    if len(word) == 0 or word[0] != 'From:':
        continue
    if word[1] not in count:
        count[word[1]] = 1
    else:
        count[word[1]] += 1


for key in count:
    if key is max(count):       #Uji nilai terbesar dalam kamus
        print(key, count[key])

#print(most)
#print(max(most))

