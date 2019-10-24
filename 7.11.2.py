# open file search some string and extract data from it
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File not found!\n\n\nExit program!!')
    exit()
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        collon = line.strip().find(':')
        desimal = float(line[collon + 1:])
        count += 1
        total = total + desimal
        print(desimal)
# print(type(desimal))
print('search count:', count)
print('Average spam confidence:', total/count)

