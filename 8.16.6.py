number = []
while True:
    try:
        inp = input('Enter a number: ')
        if inp.lower() == 'done':
            break
        else:
            g = int(inp)
            number.append(g)
    except ValueError:
        print('Bad value!')
print('the hightest number is:', max(number))
print('the lowest number is:', min(number))
