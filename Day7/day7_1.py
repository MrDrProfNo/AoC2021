"""
@author MrNo

Summary:
Given a bunch of points on a line (integers only), find a (new) point
that minimizes total distance to all other points
"""

def main():

    with open("inputs.txt", "r") as file:
        positions = sorted([int(position) for position in file.readline().strip().split(",")])

    if len(positions) % 2 == 0:
        center_1 = positions[len(positions) // 2]
        center_2 = positions[(len(positions) // 2) + 1]

        point, total_distance = max(
            (center_1, total_distance_from_value(center_1, positions)),
            (center_2, total_distance_from_value(center_2, positions)),
            key=lambda x: x[1]
        )
    else:
        point = positions[len(positions) // 2]
        total_distance = total_distance_from_value(point, positions)

    print(f"Least total distance is {total_distance} for point {point}")


def total_distance_from_value(value, iterable):
    return sum([abs(position - value) for position in iterable])


if __name__ == '__main__':
    main()
