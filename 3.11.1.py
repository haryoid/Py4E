try:
    hours = float(input('Enter hours: '))
    try:
        rate = float(input('Enter rate: '))
    except:
        if hours > 40:
            pay = (40 * rate) + ((hours - 40) * rate * 1.5)
            print('Pay:', pay)
        else:
            pay = hours * rate
            print('Pay:',  pay)
except:
    print('Invalid Value!')