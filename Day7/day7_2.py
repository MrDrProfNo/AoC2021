"""
@author MrNo

Summary:
Same as part 1, except the distance metric has changed. There's probably a
better way to do this than brute force, but brute force is easy on the input set
"""


def total_sum_distance_from_value(value, positions):
    # sum(1...n) = n(n-1)/2; run that sum on the distance between value and each position
    return sum([abs(position - value) * (abs(position-value) + 1) // 2 for position in positions])


def main():
    with open("inputs.txt", "r+") as file:
        positions = [int(val) for val in file.readline().strip().split(",")]

    # the absolutely terrible really awful oneline bruteforce
    total_distance, value = \
        min([(total_sum_distance_from_value(point, positions), point) for point in range(max(positions))])

    print(f"Least total distance is {total_distance}, for point {value}")


if __name__ == '__main__':
    main()
