fruit = input('Type a fruit: ')
index = len(fruit)
while index != 0:
    letter = fruit[index-1]
    print(letter)
    index -= 1