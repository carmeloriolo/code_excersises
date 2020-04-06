# Input: board = ["EEEEE","EEMEE","EEEEE","EEEEE"], Click : [3,0]
# Output: ["B1E1B","B1M1B","B111B","BBBBB"]

# E E E E E
# E E M E E
# E E E E E
# E E E E E [3, 0] is the first Element of this ROW

# If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B')

#  E  E
# [E] E => All the adjacents fields should be reveleade .. E = > B

# B 1 E 1 B
# B 1 M 1 B
# B 1 1 1 B
# B B B B B

# Output: [ "B1E1B", "B1M1B", "B111B", "BBBBB"]

# Click is a Mine -> GAME OVER
# if not
#      check if neighbors are mines and so on
# else if yes
#     [x,y] = M
#     return


# [2,2] x = 2; y = 2;
#    [x-1, y] L, [x+1, y] R                                            Check on the same row
#    [x, y-1] UP, [x, y+1] BOTTOM                                      Check on the same column
#    [x-1, y-1] LDU, [x+1, y-1] RDP, [x-1, y+1] LDB, [x+1, y+1 ]RDB    Check diagonals


def is_mine(field):
    if field == 'M':
        return 1
    return 0


def update_row(board, index, val):
    string_as_list = list(board[index])
    string_as_list[index] = val
    board[index] = ''.join(string_as_list)


def mine_sweeper(board, click):
    count = 0
    y = click[0]
    x = click[1]
    if is_mine(board[y][x]) == 1:
        update_row(board, y, 'X')
        return -1
    if board[y][x] == 'E':
        # check if mines are near and count it
        for i in range(y - 1, y + 2):
            if i < 0 or i >= len(board):
                continue
            for j in range(x - 1, x + 2):
                if j < 0 or j >= len(board[0]):
                    continue
                if is_mine(board[i][j]):
                    count += 1
        if count > 0:
            update_row(board, y, str(count))
        else:
            update_row(board, y, 'B')
            for i in range(y - 1, y + 1):
                if i < 0 or i >= len(board):
                    continue
                for j in range(x - 1, x + 2):
                    if j < 0 or j >= len(board[0]):
                        continue
                    click = [i, j]
                    mine_sweeper(board, click)


board = ["EEEEE",
         "EEMEE",
         "EEEEE",
         "EEEEE"]
print(board)
click = [3, 0]
mine_sweeper(board, click)
print(board)
click = [1, 2]
mine_sweeper(board, click)
print(board)
