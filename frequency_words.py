def freq_words():
    stringValue = input('Enter any input: ')
    li = stringValue.split()
    d = {}

    for i in li:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] + 1
    print(d)

freq_words()