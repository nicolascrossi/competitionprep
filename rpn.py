
class Node:

    def __init__(self):
        self.let = ''
        self.left = None
        self.right = None

    def hasChild(self):
        if (not self.left is None) or (not self.right is None):
            return True
        return False

    def __repr__(self):
        return self.let

def p(curEqn):
    first = -1
    last = -1
    for i in range(0, len(curEqn)):
        if curEqn[i].let == '(':
            if first == -1:
                first = i
        elif curEqn[i].let == ')':
            last = i
    if first == -1:
        return None

    del curEqn[last]
    del curEqn[first]


    tmp = passThrough(curEqn[first:last-1])
    for i in range(0, last - 2 - first):
        del curEqn[first]
    curEqn[first] = tmp[0]
    return curEqn

def e(curEqn):
    count = 0
    for n in reversed(curEqn):
        if n.let == '^' and not n.hasChild():
            #idx = ''.join(curEqn).rindex('^')
            idx = len(curEqn) - count - 1
            subEqn = curEqn[idx-1:idx+2]
            n.left = subEqn[0]
            n.right = subEqn[2]
            del curEqn[idx+1]
            del curEqn[idx-1]
            return passThrough(curEqn)
        count += 1
    return None

#Run until it returns none
def m(curEqn):
    for i in range(0, len(curEqn)):
        if curEqn[i].let == '*' and not curEqn[i].hasChild():
            subEqn = curEqn[i-1:i+2]
            n = subEqn[1]
            n.left = subEqn[0]
            n.right = subEqn[2]
            del curEqn[i+1]
            del curEqn[i-1]
            return passThrough(curEqn)
    return None

#Run until it returns none
def d(curEqn):
    for i in range(0, len(curEqn)):
        if curEqn[i].let == '/' and not curEqn[i].hasChild():
            subEqn = curEqn[i-1:i+2]
            n = subEqn[1]
            n.left = subEqn[0]
            n.right = subEqn[2]
            del curEqn[i+1]
            del curEqn[i-1]
            return passThrough(curEqn)
    return None

#Run until it returns none
def a(curEqn):
    for i in range(0, len(curEqn)):
        if curEqn[i].let == '+' and not curEqn[i].hasChild():
            subEqn = curEqn[i-1:i+2]
            n = subEqn[1]
            n.left = subEqn[0]
            n.right = subEqn[2]
            del curEqn[i+1]
            del curEqn[i-1]
            return passThrough(curEqn)
    return None

#Run until it returns none
def s(curEqn):
    for i in range(0, len(curEqn)):
        if curEqn[i].let == '+' and not curEqn[i].hasChild():
            subEqn = curEqn[i-1:i+2]
            n = subEqn[1]
            n.left = subEqn[0]
            n.right = subEqn[2]
            del curEqn[i+1]
            del curEqn[i-1]
            return passThrough(curEqn)
    return None

def v(curEqn):
    if len(curEqn) == 1:
        return curEqn[0]

#Takes an eqn, and runs it through the full gamut of functions
def passThrough(curEqn):

    #run p and e

    tmp = curEqn
    while True:
        tmp = p(tmp)
        if tmp is None:
            break
        curEqn = tmp

    tmp = curEqn
    while True:
        tmp = e(tmp)
        if tmp is None:
            break
        curEqn = tmp

    tmp = curEqn
    while True:
        tmp = m(tmp)
        if tmp is None:
            break
        curEqn = tmp
    
    tmp = curEqn
    while True:
        tmp = d(tmp)
        if tmp is None:
            break
        curEqn = tmp

    tmp = curEqn
    while True:
        tmp = a(tmp)
        if tmp is None:
            break
        curEqn = tmp

    tmp = curEqn
    while True:
        tmp = s(tmp)
        if tmp is None:
            break
        curEqn = tmp

    return curEqn

def lrc(n):
    if not n.left is None:
        lrc(n.left)
    if not n.right is None:
        lrc(n.right)
    print(n.let, end='')

times = int(input(""))
for i in range(0, times):
    cases = int(input(""))
    for i in range(0, cases):
        eqn = input("")

        #Turn the input string into an array of characters
        eqn = eqn.split(" ")

        #Set all elements in the array eqn to Node objects

        for i in range(0, len(eqn)):
            n = Node()
            n.let = eqn[i]
            eqn[i] = n

        lrc(passThrough(eqn)[0])
        print()

'''
a * b + c
a * b + c * d / e
a ^ b ^ c + d ^ e
( a + b ) * c
'''