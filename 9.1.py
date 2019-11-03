'''
fhand = open('words.txt')
d = dict()
for line in fhand:
    d[line] = 1
print(d)
'''


word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
lst = list(d.keys())
lst.sort()
print(lst)
for key in lst:
    print(key, d[key])


