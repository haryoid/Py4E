total = 0
count = 0
min = 0
max = 0
while True:
    try:
        promt = input('Enter a number: ')
        if promt == 'done':
            break
        else:
            number = int(promt)
            total = total + number
            count += 1
            continue
    except:
        print('Invalid value!')
avg = total/count
print('Total:', total)
print('Count:', count)
print('Average:', avg)