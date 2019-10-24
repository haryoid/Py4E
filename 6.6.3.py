def count_a_char(word,char):
    count = 0
    for letter in word:
        if letter == char:
            count += 1
    print(count)


count_a_char('banana is fruit i like', 'a')