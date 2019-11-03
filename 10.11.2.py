fname = input('Enter a file name: ')

try:
    fopen = open(fname)
except FileNotFoundError:
    print('file not found!')
    exit()

count = dict()
for line in fopen:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if len(words) == 0 or words[0] != 'From':
            continue
        delimiter = ':'
        h = words[5].split(delimiter)
        if h[0] not in count:
            count[h[0]] = 1
        else:
            count[h[0]] += 1
print(count)

lst = list()
for key, val in list(count.items()):
    lst.append((key, val))

lst.sort()
for key, val in lst:
    print(key,val)