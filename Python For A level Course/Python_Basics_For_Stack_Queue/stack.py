def push(data):
    data.append(5)
    data.append(1)
    print(data)
    print(data[len(data)-2])

def poping(data):
    data.pop()
    data.pop()
    print(data)
data = [4,3,6,8,9]
push(data)
poping(data)