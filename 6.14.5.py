str = ' X-DSPAM-Confidence:0.8475 '
a = str.strip()
collon = str.strip().find(':')
desimal = float(a[collon+1:])
#num = float(desimal)

#print('%g' % num)
print('%g' % desimal)
print(a)
print(collon)

#replace collon
new = a.replace(':', ',')
print(new)