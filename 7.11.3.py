naaboo = 'na na boo boo'
fname = input('Enter a file name: ')
if fname == naaboo:
    print(naaboo.upper(),'TOO YOU! - You have been punkd!')
else:
    count = 0
    try:
        fhand = open(fname)
    except FileNotFoundError:
        print('File not found!')
    for line in fhand:
        count += 1
    print('There were', count, 'subject in', fname)
