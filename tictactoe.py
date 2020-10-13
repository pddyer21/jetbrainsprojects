# write your code here
def isnumber(x):
    try:
        val = int(x)
        return True
    except ValueError:
        return False


def iswinner(board):
    if board[0] == board[1] == board[2] != " " and board[3:5].count("X") != 3 and board[3:5].count("O") != 3 and board[6:8].count("X") != 3 and board[6:8].count("O") != 3:
        # print("{} wins".format(board[0]))
        return [True, board[0]]
    elif board[3] == board[4] == board[5] != " " and board[0:2].count("X") != 3 and board[0:2].count("O") != 3 and board[6:8].count("X") != 3 and board[6:8].count("O") != 3:
        # print("{} wins".format(board[3]))
        return [True, board[3]]
    elif board[6] == board[7] == board[8] != " " and board[0:2].count("X") != 3 and board[0:2].count("O") != 3 and board[3:5].count("X") != 3 and board[3:5].count("O") != 3:
        # print("{} wins".format(board[6]))
        return [True, board[6]]
    elif board[0] == board[3] == board[6] != " " and ([board[1], board[4], board[7]] != ["X", "X", "X"] and [board[1], board[4], board[7]] != ["O", "O", "O"]) and ([board[2], board[5], board[8]] != ["X", "X", "X"] and [board[2], board[5], board[8]] != ["O", "O", "O"]):
        # print("{} wins".format(board[0]))
        return [True, board[0]]
    elif board[1] == board[4] == board[7] != " " and ([board[0], board[3], board[6]] != ["X", "X", "X"] and [board[0], board[3], board[6]] != ["O", "O", "O"]) and ([board[2], board[5], board[8]] != ["X", "X", "X"] and [board[2], board[5], board[8]] != ["O", "O", "O"]):
        # print("{} wins".format(board[1]))
        return [True, board[1]]
    elif board[2] == board[5] == board[8] != " " and ([board[0], board[3], board[6]] != ["X", "X", "X"] and [board[0], board[3], board[6]] != ["O", "O", "O"]) and ([board[1], board[4], board[7]] != ["X", "X", "X"] and [board[1], board[4], board[7]] != ["O", "O", "O"]):
        # print("{} wins".format(board[2]))
        return [True, board[2]]
    elif board[0] == board[4] == board[8] != " ":
        # print("{} wins".format(board[0]))
        return [True, board[0]]
    elif board[2] == board[4] == board[6] != " ":
        # print("{} wins".format(board[2]))
        return [True, board[2]]
    else:
        return [False, None]


def prtbrd(board):
    toprow = board[:3]
    middlerow = board[3:6]
    bottomrow = board[6:10]
    print("---------")
    print("| {} {} {} |".format(toprow[0], toprow[1], toprow[2]))
    print("| {} {} {} |".format(middlerow[0], middlerow[1], middlerow[2]))
    print("| {} {} {} |".format(bottomrow[0], bottomrow[1], bottomrow[2]))
    print("---------")
    return None


def gameplay(cells):
    player = 0
    plays = ["X", "O"]
    coords = {(1, 1): 6, (1, 2): 3, (1, 3): 0, (2, 1): 7, (2, 2): 4, (2, 3): 1, (3, 1): 8, (3, 2): 5, (3, 3): 2}
    while True:
        column, row = input("Enter the coordinates: >").split()
        if isnumber(column) and isnumber(row):
            col = int(column)
            rw = int(row)
            if col in [1, 2, 3] and rw in [1, 2, 3]:
                if cells[coords[col, rw]] == " " or cells[coords[col, rw]] == "_":
                    if player == 0:
                        cells[coords[col, rw]] = plays[player]
                        player += 1
                        prtbrd(cells)
                        winner = iswinner(cells)
                        if winner[0]:
                            return winner[1]
                        elif cells.count("_") == 0 and cells.count(" ") == 0 and not winner[0]:
                            return "Draw"
                        else:
                            continue
                    else:
                        cells[coords[col, rw]] = plays[player]
                        player -= 1
                        prtbrd(cells)
                        winner = iswinner(cells)
                        if winner[0]:
                            return winner[1]
                        elif cells.count("_") == 0 and cells.count(" ") == 0 and not winner[0]:
                            return "Draw"
                        else:
                            continue
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


# Start game
brd = [" " for i in range(9)]
prtbrd(brd)
result = gameplay(brd)
if result in ["X", "O"]:
    print("{} wins".format(result))
else:
    print(result)
