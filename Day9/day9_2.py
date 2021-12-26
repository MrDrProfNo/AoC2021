"""
@author MrNo

Summary:
Grid of values representing heights, find the local-minimum points and
flood-fill outwards from them until you hit
"""
from day9_1 import in_bounds
import collections


# def get_basin_size(point: tuple[int, int], grid, previous: tuple[int, int]=None):
#     """
#     Flood-fills outward from any point, calculating how large its basin is.
#
#     Only recursive invocations should use the previous parameter
#     """
#
#     value = grid[point[0]][point[1]]
#     previous_value = grid[previous[0]][previous[1]] if previous else 0
#
#     if value == 9:
#         return 0
#     elif value > previous_value:
#         return 1 + sum(get_basin_size(adjacent, grid, point) for adjacent in get_adjacent(point, grid) if adjacent != previous)
#     else:
#         return 0


def get_basin_size(point: tuple[int, int], grid):
    remaining = collections.deque()
    remaining.append(point)
    touched = 0
    visited = [[False for _ in row] for row in grid]

    while not len(remaining) == 0:
        current = remaining.popleft()
        value = grid[current[0]][current[1]]
        if value == 9:
            continue
        else:
            touched += 1

        visited[current[0]][current[1]] = True

        adjacencies = get_adjacent(current, grid)
        for adjacent in adjacencies:
            adjacent_value = grid[adjacent[0]][adjacent[1]]
            if adjacent in remaining or adjacent_value == 9 or visited[adjacent[0]][adjacent[1]]:
                continue
            elif adjacent_value > value:
                remaining.append(adjacent)

    # For use in debugging. Do not uncomment with large inputs.

    # for line in visited:
    #     for cell in line:
    #         print(f"{cell:1}", end="")
    #     print()
    return touched


def get_adjacent(point: tuple[int, int], grid):
    """
    Gets all straight-adjacent points to the given point in the given 2D-array. "grid" is
    assumed to be rectangular. Points out of bound will not be included.
    """
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for offset in offsets:
        adjacent = point[0] + offset[0], point[1] + offset[1]
        if in_bounds(adjacent, grid):
            yield adjacent


def main():
    depths = []
    with open("inputs.txt", "r") as file:
        for row_number, line in enumerate(file):
            depths.append([])
            for char in line.strip():
                depths[row_number].append(int(char))

    basin_sizes = []
    for row_number, row in enumerate(depths):
        for col_number, val in enumerate(row):
            point = row_number, col_number
            adjacencies = get_adjacent(point, depths)
            if val < min(depths[adjacent[0]][adjacent[1]] for adjacent in adjacencies):
                basin_sizes.append(get_basin_size(point, depths))

    basin_sizes.sort(reverse=True)
    product = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    print(f"Got three largest basins: {basin_sizes[0]}, {basin_sizes[1]}, {basin_sizes[2]} with product {product}")


if __name__ == '__main__':
    main()
