import re
fname = input('Enter a file name: ')

try:
    fopen = open(fname)
except FileNotFoundError:
    print('File not found!')
    exit()

count = 0
t = list()
for line in fopen:
    line = line.rstrip()
    x = re.findall('^New.*: ([0-9]+)', line)
    if len(x) > 0:
        t = t + x           #mengembalikan hasil findall() berupa list menjadi string ke dalam list t. jika menggunakan append() t menjadi list of singleton list
        count += 1

total = 0
for index in t:
    index = int(index)
    total = total + index

avg = total/count
print(int(avg))