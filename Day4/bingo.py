"""
@author MrNo

A board is a DIM x DIM array of spaces, with each space containing
a string (numeric), and being either marked or unmarked.
"""


class BingoBoard:
    def __init__(self, state: list[list[str]]):
        self.state: list[list[BingoSpace]] = [[BingoSpace(value) for value in row] for row in state]

    def score(self):
        return sum(
            int(space.value) for row in self.state for space in row if not space.is_marked()
        )

    def mark(self, value):
        for row in self.state:
            for space in row:
                if space.value == value:
                    if space.is_marked():
                        raise ValueError(f"Attempted to mark space that is already marked: {space.value}")
                    else:
                        space.set_marked()
                        return

    def mark_position(self, x, y):
        if self.state[x][y].is_marked():
            raise ValueError(f"Attempted to mark space that is already marked: {x},{y}")
        else:
            self.state[x][y].set_marked()

    def has_won(self):
        for row in self.state:
            for space in row:
                if not space.is_marked():
                    break
            else:
                return True
        for col_index in range(len(self.state[0])):
            for row_index in range(len(self.state[0])):
                if not self.state[row_index][col_index].is_marked():
                    break
            else:
                return True

        return False

    def __str__(self):
        return "\n".join([",".join([str(val) for val in row]) for row in self.state])


class BingoSpace:
    def __init__(self, value: str):
        self.value: str = value
        self.marked: bool = False

    def set_marked(self):
        self.marked = True

    def is_marked(self):
        return self.marked

    def __str__(self):
        if self.is_marked():
            return self.value + "*"
        else:
            return self.value
