"""
@author MrNo

Summary:
The same as day 1, except performed with a sliding window of width 3

It was later pointed out that if you're comparing (a + b + c) < (b + c + d), that's actually just comparing a < d. The
alternative implementation found in improved() (not used within this script) takes advantage of that
"""


def main():
    filename = "inputs.txt"
    with open(filename, "r") as file:
        depths = [int(depth) for depth in file.readlines()]
    windows = [window for window in sliding_window(depths, 3)]
    print("Number of steps increasing:",
          sum(sum(window) > sum(windows[index]) for index, window in enumerate(windows[1:])))


def sliding_window(iterable, width):
    for i in range(0, len(iterable) - width + 1):
        yield iterable[i:i+width]


def improved():
    filename = "inputs.txt"
    with open(filename, "r") as file:
        depths = [int(depth) for depth in file.readlines()]

    print("Number of steps increasing:", sum(val > depths[index] for index, val in enumerate(depths[3:])))


if __name__ == "__main__":
    main()
    # improved()
