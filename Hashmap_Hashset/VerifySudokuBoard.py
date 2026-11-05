board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


def verifySudokuBoard(board: list[list[str]]) -> bool:
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(len(board)):
        for c in range(len(board[0])):
            val = board[r][c]
            if val == ".":
                continue

            if val in row_sets[r]:
                return False

            if val in col_sets[c]:
                return False

            if val in subgrid_sets[r // 3][c // 3]:
                return False

            row_sets[r].add(val)
            col_sets[c].add(val)
            subgrid_sets[r // 3][c // 3].add(val)
    return True


def verifySudokuBoard(board: list[list[str]]) -> bool:
    for i in range(len(board)):
         hash_set = set()
         for j in range(len(board[0])):
             if board[i][j] == ".":
                 continue
             if board[i][j] in hash_set:
                 return False
             # print(board[i][j])
             hash_set.add(board[i][j])

    for i in range(len(board[0])):
         hash_set = set()
         for j in range(len(board)):
             if board[j][i] == ".":
                 continue
             if board[j][i] in hash_set:
                 return False
             hash_set.add(board[j][i])

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            hash_set = set()
            for i in range(3):
                for j in range(3):
                    value = board[box_row + i][box_col + j]
                    if value == ".":
                        continue
                    if value in hash_set:
                        return False
                    hash_set.add(value)

    return True

print(verifySudokuBoard(board))
print(verifySudokuBoard(board))