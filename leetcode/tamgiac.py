
for i in range(10):
    string = ''
    for x in range(i, 10):
        if string == '':
            string += str(x)
        else:
            string += ' ' + str(x)
    print(string)
