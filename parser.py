def splitter (x, y):
    return x.split(y)

def parser (x):
    data = splitter(x,"=")
    result = []
    for i in range(0,len(data),1):
        result.append(int(data[i]))
    return result

