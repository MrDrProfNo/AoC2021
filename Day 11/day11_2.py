"""
@author MrNo

Summary:
Building on part 1, find the first generation on which all cells flash
"""
from day11_1 import flash


def main():
    grid = []
    with open("inputs.txt", "r") as file:
        for line in file:
            grid.append([int(char) for char in line.strip()])

    print("Generation 0: ")
    print(*[row for row in grid], sep="\n")

    cell_count = len(grid) * len(grid[0])

    # looping until all have flashed this time
    current_generation = 0
    while True:
        for x, row in enumerate(grid):
            for y in range(len(row)):
                grid[x][y] += 1
                value = grid[x][y]
                if value > 9:
                    flash((x, y), grid)

        # we only care about how many flashed in any individual run now.
        flashes = 0

        # reset everything that flashed to 0, and count number of flashes
        for x, row in enumerate(grid):
            for y, value in enumerate(row):
                if value > 9:
                    grid[x][y] = 0
                    flashes += 1

        print(f"\nGeneration: {current_generation + 1}")
        print(*[row for row in grid], sep="\n")

        if flashes == cell_count:
            break


        current_generation += 1

    print(f"On generation {current_generation + 1 }, all cells ({flashes}) flashed")


if __name__ == '__main__':
    main()
