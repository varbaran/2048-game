from utils.board import *
from utils.random_helpers import choose_random, generate_random


def main():
    board = generate_empty_board()
    for _ in range(2):
        cells = empty_cells(board)
        i, j = choose_random(cells)
        rand = generate_random()
        board[i][j] = rand
    for r in board:
        print(r)
    print()
    while not is_winner(board):
        print("d moves downward\nu moves upward\nl moves leftward\nr moves rightward")
        move = input("which direction you want to move?")
        if move == "d":
            board = move_down(board)
            board = merge_down(board)
            board = move_down(board)
        elif move == "u":
            board = move_up(board)
            board = merge_up(board)
            board = move_up(board)
        elif move == "r":
            board = move_right(board)
            board = merge_right(board)
            board = move_right(board)
        elif move == "l":
            board = move_left(board)
            board = merge_left(board)
            board = move_left(board)
        cells = empty_cells(board)
        if len(cells) == 0 and not check_similar_numbers(board):
            break
        elif len(cells) > 0:
            i, j = choose_random(cells)
            rand = generate_random()
            board[i][j] = rand

        for r in board:
            print(r)
        print()
    for r in board:
        print(r)
    print()
    if is_winner(board):
        print("You won!")
    else:
        print("Game over!")


if __name__ == '__main__':
    main()
