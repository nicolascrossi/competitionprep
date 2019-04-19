from collections import deque

for i in range(0, 5):
    stack = deque()
    eqn = input("")
    eqn = eqn.split(" ")
    eqn.reverse()
    for i in eqn:
        try:
            stack.append(int(i))
        except:
            if i == '|':
                o1 = int(stack.pop())
                o1 = abs(o1)
                stack.append(o1)
            elif i == '+':
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                stack.append(o1 + o2)
            elif i == '-':
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                stack.append(o1 - o2)
            elif i == '*':
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                stack.append(o1 * o2)
            elif i == '@':
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                o3 = int(stack.pop())
                if o1 >= 0:
                    stack.append(o2)
                else:
                    stack.append(o3)
            elif i == '>':
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                o3 = int(stack.pop())
                stack.append(max([o1, o2, o3]))
    print(stack.pop())
'''
* + 4 5 - 3 -1
@ - 8 9 82 46
@ | - -8 10 82 46
+ > 8 * 2 7 9 6
| * @ - 1 6 34 12 > - 990 1000 * -2 3 + -51 49
'''