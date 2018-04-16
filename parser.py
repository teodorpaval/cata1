def parser (x):
    numbers = []
    operations = []
    for i in range(0, len(x)-1):
        if i % 2 == 0:
            numbers.append(int(x[i]))
        else:
            operations.append(x[i])
    return numbers,operations

print(parser("8+3=9 "))