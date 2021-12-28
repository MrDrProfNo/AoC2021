"""
@author MrNo

Summary:
Given a 2d-array of numbers, have them all count up until they're above 9 and "flash", then reset them to 0.

Flashes increment adjacent cells, allowing chain flashes

Run multiple iterations, count how many flashes occur.
"""
MAX_GENERATIONS = 100


def get_adjacent_points(point: tuple[int, int], grid):
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for offset in offsets:
        adjacent = point[0] + offset[0], point[1] + offset[1]
        if in_bounds(adjacent, grid):
            yield adjacent


def in_bounds(point: tuple[int, int], grid):
    """
    Checks if a given point is in bounds for a given 2D array. All rows are assumed to have
    the same length as the first row.
    """
    xDim = len(grid)
    yDim = len(grid[0])

    return 0 <= point[0] < xDim and 0 <= point[1] < yDim


def flash(point: tuple[int, int], grid):
    """
    Runs the flashing logic at a given point, and chains if applicable

    Basic logic is: for each adjacent cell, increment it by one. If its value is now > 9,
    flash it. Perform for all cells
    """
    if grid[point[0]][point[1]] != 10:
        return

    for adjacent in get_adjacent_points(point, grid):
        grid[adjacent[0]][adjacent[1]] += 1

        flash(adjacent, grid)


def main():
    grid = []
    with open("inputs.txt", "r") as file:
        for line in file:
            grid.append([int(char) for char in line.strip()])


    flashes = 0



    print("Generation 0: ")
    print(*[row for row in grid], sep="\n")

    for i in range(MAX_GENERATIONS):
        for x, row in enumerate(grid):
            for y in range(len(row)):
                grid[x][y] += 1
                value = grid[x][y]
                if value > 9:
                    flash((x, y), grid)

        # reset everything that flashed to 0
        for x, row in enumerate(grid):
            for y, value in enumerate(row):
                if value > 9:
                    grid[x][y] = 0
                    flashes += 1

        print(f"\nGeneration: {i + 1}")
        print(*[row for row in grid], sep="\n")

    print(f"After {MAX_GENERATIONS} iterations, there were {flashes} flashes")


if __name__ == '__main__':
    print(list(get_adjacent_points((1, 1), [[0 for _ in range(10)] for _ in range(10)])))
    main()
