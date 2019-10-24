total = 0
count = 0
while True:
    try:
        num = int(input('enter number: '))
        again = input('another number (Y/N)?\n ')
        total = total + num
        count += 1
        if again == 'y' or again == 'Y':
            continue
        elif again == 'n' or again == 'N':
            break
        else:
            print('That means No!')
            break
    except ValueError:
        print('Invalid command!')
print('you entered number', count, 'times')
print('and have total value', total)


