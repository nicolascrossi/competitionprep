class Node:

    def __init__(self):
        self.children = []
        self.board = None
        self.score = None
        #True if X
        self.newMove = None
        self.turn = None
        self.winning = False

#True if X turn
def genTree(board, turn):
    print("RUNNING")
    new = Node()
    new.board = board
    new.turn = turn
    win = checkWin(board)
    print("win", win)
    if win == 1:
        new.score = 1
        new.winning = True
    elif win == 2:
        new.score = -1
    elif win == 3:
        print(board[0])
        print(board[1])
        print(board[2])
        new.score = 0
    elif win == 0:
        for i in range(0, 3):
            for j in range(0, 3):
                space = board[i][j]
                print('space')
                if space == '*':
                    print("new child")
                    newB = board.copy()
                    if turn:
                        newB[i][j] = 'X'
                    else:
                        newB[i][j] = 'O'
                    print(newB[0])
                    print(newB[1])
                    print(newB[2])
                    child = genTree(newB, not turn)
                    new.children.append(child)
                    child.newMove = (i, j)
        minmax = None
        for c in new.children:
            if minmax is None:
                minmax = c.score
            elif turn:
                if minmax < c.score:
                    minmax = c.score
            else:
                if minmax > c.score:
                    minmax = c.score
    print('newscore', new.score)
    return new

#Return 0 if unfinished, 1 if win, 2 if lose, 3 if draw
#DOESN"T CHECK VERTICAL
def checkWin(board):
    full = True
    for row in board:
        won = True
        cur = row[0]
        for space in row:
            if space == '*':
                full = False
            #print(cur == space)
            if cur == '*' or not cur == space:
                won = False
                break
        if won:
            #print(row)
            if cur == 'X':
                return 1
            else:
                return 2
    if full:
        return 3
    #print("0")
    #print(board[0])
    #print(board[1])
    #print(board[2])
    return 0

games = int(input(""))

for g in range(0, games):
    rows = []
    for i in range(0, 3):
        rows.append(list(input("")))
    print(rows)
    #rows[row][col]
    root = genTree(rows, True)
    maxScore = -2
    move = None
    for c in root.children:
        if c.winning:
            move = c.newMove
            break
        if c.score > maxScore:
            maxScore = c.score
            move = c.newMove
    rows[move[0]][move[1]] = 'X'
    print(rows)

#CURRENTLY THE WIN CHECK IS VERY BROKEN
'''
2
OOX
X*O
**X
'''