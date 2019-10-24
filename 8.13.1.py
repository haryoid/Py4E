def chop(t):
    del t[len(t)-1]
    del t[0]
    return t

def middle(t):
    t = t[1:len(t)-1]
    return t

number = [1,2,3,4,5,6]
print(middle(number))