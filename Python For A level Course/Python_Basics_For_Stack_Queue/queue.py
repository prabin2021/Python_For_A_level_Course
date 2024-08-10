from collections import deque
def enqueuing():
    data = deque()
    data.append("hi")
    data.append("hey")
    data.append("hello")
    print(data)
    data.popleft()
    print(data)

enqueuing()
