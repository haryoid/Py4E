'''
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.
'''

fname = input('Enter a file name: ')

try:
    fopen = open(fname)
except FileNotFoundError:
    print('File not found!')
    exit()

count = dict()
for line in fopen:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if len(words) == 0 or words[0] != 'From':
            continue
        if words[1] not in count:
            count[words[1]] = 1
        else:
            count[words[1]] += 1

#print(count)

lst = list()
for key, val in list(count.items()):
    lst.append((val,key))

lst.sort(reverse=True)
#print(lst)

count, mail = max(lst)
print('most commits: ', mail + ',', count, 'times')

count, mail = min(lst)
print('least commits: ', mail + ',', count, 'times')



