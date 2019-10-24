total = 0
count = 0
min = None
max = None
while True:
    try:
        promt = input('Enter a number: ')
        if promt == 'done':
            break
        else:
            number = int(promt)
            if min is None or number < min:
                min = number
            if max is None or number > max:
                max = number
            total = total + number
            count += 1
            continue
    except:
        print('Invalid value!')

print('Total:', total)
print('Count:', count)
print(min, max)