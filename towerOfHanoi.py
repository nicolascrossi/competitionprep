from collections import deque

times = int(input(""))
for i in range(0, times):
    amt = int(input(""))

    a = deque()
    b = deque()
    c = deque()
    
    for j in range(0, amt):
        a.append(amt-j)

    