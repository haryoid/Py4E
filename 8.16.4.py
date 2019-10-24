finput = input('Enter a file name: ')
fopen = open(finput)
alphabet = []
for line in fopen:
    words = line.split()
    #print(words)
    for word in words:
        if word not in alphabet:
            alphabet.append(word)
        #print(word)
alphabet.sort()
print(alphabet)


