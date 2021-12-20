"""
@author MrNo

Summary:
Basically just simulating a game of bingo from input files incl. the numbers to be drawn,
"""

import re
from bingo import BingoBoard

filename = "inputs.txt"


def run_until_winner(boards, moves):
    winner = None
    for move in moves:
        for board in boards:
            board.mark(move)
            if board.has_won():
                winner = board
        if winner:
            return winner, move, board.score()


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

        (winner, move, score) = run_until_winner(boards, moves)

        scores = [board.score() for board in boards]

        print(f"On move {move} got winner\n{winner}\nwith score {score}")

        print(f"All boards that won:\n", "\n\n".join([str(board) for board in boards if board.has_won()]))


if __name__ == '__main__':
    main()
