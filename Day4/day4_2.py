"""
@author MrNo

Summary:
Basically just simulating a game of bingo from input files incl. the numbers to be drawn

4-2 varies in that you're trying to find the last board that wins instead of the first
"""

import re
from bingo import BingoBoard

filename = "inputs.txt"


def run_until_finished(boards: list[BingoBoard], moves: list[str]):
    """
    Runs the given number pulls on the passed boards until all boards have won
    :param boards: list of BingoBoard objects, populated
    :param moves: list of numbers pulled for the game
    :return:
    """
    for move in moves:
        for board in boards:
            board.mark(move)
        boards = [board for board in boards if not board.has_won()]

        # board is guaranteed to be assigned, despite what the linter says
        if len(boards) == 0:
            return board, move, board.score()


def main():
    with open(filename, "r") as file:
        moves = file.readline().strip().split(",")

        boards: list[BingoBoard] = []

        while line := file.readline():
            if line == "\n":
                continue

            # regex is used to split without producing empty strings
            board = [re.split(r" +", line.strip())]

            # we've already got one line; read the next 4
            for i in range(4):
                board.append(re.split(r" +", file.readline().strip()))

            boards.append(BingoBoard(board))

        (winner, move, score) = run_until_finished(boards, moves)

        scores = [board.score() for board in boards]

        print(f"On move {move}, final board \n{winner}\nwon with score {score}")


if __name__ == '__main__':
    main()
