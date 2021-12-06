class bingoBoard:
    def __init__(self, size):
        self.board = []
        self.size = size

    def addRow(self, row):
        self.board.append(row)

    def row(self, idx):
        tmp = []
        for i, item in enumerate(self.board[idx]):
            tmp.append(self.board[idx][i])
        return tmp

    def column(self, idx):
        tmp = []
        for i, item in enumerate(self.board):
            tmp.append(item[idx])
        return tmp

    def rewrite(self, x, y, value):
        self.board[x][y] = value

    def mark(self, number):
        i = 0
        while i < self.size:
            for idx, item in enumerate(self.row(i)):
                if item == number:
                    self.rewrite(i, idx, 'm')
            i += 1

    def winnerRow(self, idx):
        for item in self.row(idx):
            if item != 'm':
                return False
        return True

    def winnerColumn(self, idx):
        for item in self.column(idx):
            if item != 'm':
                return False
        return True

    def winnerBoard(self):
        for idx in range(self.size):
            if self.winnerRow(idx) or self.winnerColumn(idx):
                return True
        return False

    def winnerCount(self):
        count = 0
        for i in range(self.size):
            for item in self.row(i):
                if item != 'm':
                    count += item
        return count


b = bingoBoard(2)
b.addRow([10, 15])
b.addRow([2, 4])
b.mark(2)
b.mark(4)


def unpack():
    with open('input4') as data:
        nums = list(map(int, data.readline().split(',')))
        tmp = [item.strip() for item in data.readlines()]
    for i, e in enumerate(tmp):
        tmp[i] = list(map(int, e.split()))
    tmp = [item for item in tmp if item]
    board = bingoBoard(5)
    lst = []
    i = 0
    while i < len(tmp):
        for j in range(i, i + 5):
            board.addRow(tmp[j])
        lst.append(board)
        board = bingoBoard(5)
        i += 5
    return lst, nums

def solution():
    boards, nums = unpack()
    for num in nums:
        for board in boards:
            board.mark(num)
        for j, board in enumerate(boards):
            if board.winnerBoard():
                return num * board.winnerCount()



def solutionP2():
    boards, nums = unpack()
    lastnum = 0
    lastboard = 0
    for num in nums:
        tr = []
        for board in boards:
            board.mark(num)
            if not board.winnerBoard():
                tr.append(board)
            else:
                lastboard = board
                lastnum = num
        boards = tr
    return lastnum * lastboard.winnerCount()



