number = int(1)

for i in range(1, 10) :
    for j in range(1, 10) :
        print(str(i) + ' x ' + str(j) + ' = ' + str(i * j))
        j += 1
    i += i

