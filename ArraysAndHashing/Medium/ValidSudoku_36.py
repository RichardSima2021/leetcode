def isValidSudoku(board):
    def checkRows():
        for row in board:
            rowset = set()
            for num_str in row:
                num = 0
                if num_str == ".":
                    continue
                else:
                    num = int(num_str)
                if not 1 <= num <= 9:
                    return False
                elif num in rowset:
                    return False
                else:
                    rowset.add(num)
        # print('passed checkrows')
        return True

    def checkCols():
        for i in range(9):
            # col
            colset = set()
            sum = 0
            for c in range(9):
                num = 0
                if board[c][i] == ".":
                    continue
                else:
                    num = int(board[c][i])
                if not 1 <= num <= 9:
                    return False
                elif num in colset:
                    return False
                else:
                    colset.add(num)
        # print('passed checkcols')
        return True

    def checkGrids():
        for grid_x in range(3):
            for grid_y in range(3):
                gridset = set()
                for dx in range(3):
                    for dy in range(3):
                        num = 0
                        if board[grid_x * 3 + dx][grid_y * 3 + dy] == ".":
                            continue
                        else:
                            num = int(board[grid_x * 3 + dx][grid_y * 3 + dy])
                        if not 1 <= num <= 9:
                            return False
                        elif num in gridset:
                            return False
                        else:
                            gridset.add(num)
        # print('passed checkgrids')
        return True

    return checkRows() and checkCols() and checkGrids()