"""
@author MrNo

Summary:
We're now being asked to track state within a call. Given a list of instructions, and an associated integer, alter
the two variables "horizontal" and "depth":

if "down": increase depth
if "up": decrease depth
if "forward": increase horizontal

At the end, give the product of horizontal and depth
"""


def main():
    filename = "inputs.txt"
    with open(filename, "r") as file:

        horizontal = 0
        depth = 0

        # The first letter is enough to distinguish them, and the number is always 1-digit.
        # -2 avoids the newline character, which I don't bother stripping.
        for instruction in file:
            if instruction[0] == "d":
                depth += int(instruction[-2])
            elif instruction[0] == "u":
                depth -= int(instruction[-2])
            elif instruction[0] == "f":
                horizontal += int(instruction[-2])

        print(f"{horizontal=}, {depth=} with product: {horizontal * depth}")


if __name__ == '__main__':
    main()
