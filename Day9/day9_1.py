"""
@author MrNo

Summary:
Grid of values representing heights, find the local-minimum points and
do some math on them to prove you did it right
"""


def get_adjacent_values(point: tuple[int, int], grid):
    """
    Gets the values of all straight-adjacent points to the given point in the given
    2D-array. "grid" is assumed to be rectangular. Points out of bound will not be included.
    """
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for offset in offsets:
        adjacent = point[0] + offset[0], point[1] + offset[1]
        if in_bounds(adjacent, grid):
            yield grid[adjacent[0]][adjacent[1]]


def in_bounds(point: tuple[int, int], grid):
    """
    Checks if a given point is in bounds for a given 2D array. All rows are assumed to have
    the same length as the first row.
    """
    xDim = len(grid)
    yDim = len(grid[0])

    return 0 <= point[0] < xDim and 0 <= point[1] < yDim


def main():
    depths = []
    with open("inputs.txt", "r") as file:
        for row_number, line in enumerate(file):
            depths.append([])
            for char in line.strip():
                depths[row_number].append(int(char))

    total_risk_rating = 0
    for row_index, row in enumerate(depths):
        for col_index, value in enumerate(row):
            if value < min(get_adjacent_values((row_index, col_index), depths)):
                total_risk_rating += value + 1

    print(f"Total risk levels of all local minimums: {total_risk_rating}")


if __name__ == '__main__':
    main()
