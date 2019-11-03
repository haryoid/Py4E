import string

fname = input('Enter a file name: ')        #romeo-full.txt

try:
    fopen= open(fname)
except FileNotFoundError:
    print('File not found!')
    exit()
number = [0,1,2,3,4,5,6,7,8,9]
alphabet = dict()
for line in fopen:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', str(number)))
    line = line.lower()
    words = line.split()
    for word in words:
        for char in word:
            if char not in alphabet:
                alphabet[char] = 1
            else:
                alphabet[char] += 1
#print(alphabet)
#print(str(number))

#short dictionary
lst = list()
total = 0
for key, val in list(alphabet.items()):
    total = total + val
    lst.append((key, val))

lst.sort()
print('letter', '\tcount', '\tpercentage')
for key, val in lst:
    print('\t' ,key, '\t' ,val, '\t' ,val/total*100, '%')
