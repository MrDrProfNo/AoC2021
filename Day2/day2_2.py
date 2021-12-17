"""
@author MrNo

Summary:
An alteration on the previous day, the "up" and "down" instructions now alter an "aim" variable. When you get a
"forward" instruction, add the value to horizontal, and the value * aim to depth
"""


def main():
    filename = "inputs.txt"
    with open(filename, "r") as file:

        horizontal = 0
        depth = 0
        aim = 0

        # The first letter is enough to distinguish them, and the number is always 1-digit.
        # -2 avoids the newline character, which I don't bother stripping.
        for instruction in file:
            if instruction[0] == "d":
                aim += int(instruction[-2])
            elif instruction[0] == "u":
                aim -= int(instruction[-2])
            elif instruction[0] == "f":
                distance = int(instruction[-2])
                horizontal += distance
                depth += distance * aim

        print(f"{horizontal=}, {depth=} with product: {horizontal * depth}")


if __name__ == '__main__':
    main()