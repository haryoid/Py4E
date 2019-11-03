import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    for word in words:
        if word not in counts:
            counts[words] = 1
        else:
            counts[words] += 1

lst = list()
for key, val in list(count.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)
