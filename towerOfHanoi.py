from collections import deque

even = True
qs = None
moveL = []
moveD = {0:'A', 1:'B', 2:'C'}

def move(s, e):
    qs[e].append(qs[s].pop())
    moveL.append(moveD[s] + ' To ' + moveD[e])

#Start indicates whether this is a whole stack being moved or not
def moveStack(s, e, depth, start = None):
    moves = [0, 1, 2]
    moves.remove(s)
    moves.remove(e)
    moves = moves[0]
    if depth == 1:
        move(s, e)
    else:
        if depth%2 == 0:
            if start == True:
                moveStack(s, moves, depth-1)
                move(s, e)
                moveStack(moves, e, depth-1)
            else:
                moveStack(s, e, depth-1)
                move(s, moves)
                moveStack(e, moves, depth-1, start = True)
        else:
            moveStack(s, e, depth-1)
            move(s, e)
            moveStack(moves, e, depth-1, start = True)

a = None
b = None
c = None

times = int(input(""))
for i in range(0, times):
    amt = int(input(""))
    if amt%2 != 0:
        even = False
    a = deque()
    b = deque()
    c = deque()
    qs = [a, b, c]
    for j in range(0, amt):
        a.append(amt-j)

    moveStack(0, 2, amt, True)
    print(a)
    print(b)
    print(c)
    for m in moveL:
        print(m)