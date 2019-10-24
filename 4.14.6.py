def computepay(rate, hours):
    pay = rate * hours
    return pay

print('Pay: ', computepay(float(input('Input Rate: ')),float(input('Input hours: ')) ))