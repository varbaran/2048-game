def print_board(board):
    new_list = ""
    for lists in board:
        new_list += "|"
        for element in lists:
            if element == 0:
                new_list += "\t|"
            else:
                new_list += str(element) + "|"

        new_list += "\n"
    new_list += "\n"
    return new_list


def generate_empty_board():
    board = []
    for i in range(4):
        board.append([])
        for j in range(4):
            board[i].append(0)
    return board


def empty_cells(board):
    empty_list = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                empty_list.append([i, j])
    return empty_list


def merge_left(board):
    for i in range(len(board)):
        for j in range(len(board[i]) - 1):
            if board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                board[i][j + 1] = 0
    return board


def merge_right(board):
    for i in range(len(board)):
        for j in range(len(board[i]) - 1, 0, -1):
            if board[i][j] == board[i][j - 1]:
                board[i][j] *= 2
                board[i][j - 1] = 0
    return board


def merge_up(board):
    for i in range(len(board) - 1):
        for j in range(len(board[i])):
            if board[i][j] == board[i + 1][j]:
                board[i][j] *= 2
                board[i + 1][j] = 0
    return board


def merge_down(board):
    for i in range(len(board) - 1, 0, -1):
        for j in range(len(board[i])):
            if board[i][j] == board[i - 1][j]:
                board[i][j] *= 2
                board[i - 1][j] = 0
    return board


def check_similar_numbers(board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            for direction in directions:
                if 0 <= direction[0] + i < len(board) and 0 <= direction[1] + j < len(board[i]):
                    if board[i][j] == board[i + direction[0]][j + direction[1]]:
                        return True
    return False


def move_up(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                for k in range(i, len(board)):
                    if board[k][j] != 0:
                        board[i][j] = board[k][j]
                        board[k][j] = 0
                        break
    return board


def move_down(board):
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                for k in range(i, -1, -1):
                    if board[k][j] != 0:
                        board[i][j] = board[k][j]
                        board[k][j] = 0
                        break
    return board


def move_right(board):
    for i in range(len(board)):
        for j in range(len(board[i]) - 1, -1, -1):
            if board[i][j] == 0:
                for k in range(j, -1, -1):
                    if board[i][k] != 0:
                        board[i][j] = board[i][k]
                        board[i][k] = 0
                        break
    return board


def move_left(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                for k in range(j, len(board[i])):
                    if board[i][k] != 0:
                        board[i][j] = board[i][k]
                        board[i][k] = 0
                        break
    return board


def is_winner(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2048:
                return True
    return False
