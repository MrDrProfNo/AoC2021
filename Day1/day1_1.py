"""
@author MrNo

In general I'm going to summarize the problem here without the fluff of the story.

Today's boils down to "given a list of integers, count the number of times that an integer is greater than the one
that came immediately before it"
"""


def main():
    filename = "inputs.txt"
    with open(filename, "r") as file:
        depths = [int(depth) for depth in file.readlines()]

    print("Number of steps increasing:", sum(val > depths[index] for index, val in enumerate(depths[1:])))


if __name__ == "__main__":
    main()
