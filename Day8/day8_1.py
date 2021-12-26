"""
@author MrNo

Summary:
This is... interesting. And hard to summarize. It has the feel of an old magazine puzzle game.

You're given a series of letters, corresponding to positions in a 7-segment numeric display.
You don't know what positions though.

Part 1 is just to pull out the easy pickings - since 1, 4, 7, and 8 use a unique number of bars,
you can easily spot them in the list.
"""
from display_data import DisplaySet


def main():
    with open("inputs.txt", "r+") as file:
        displays: list[DisplaySet] = [DisplaySet(line.strip()) for line in file.readlines()]

    unique_lengths = [2, 3, 4, 7]
    #
    # for display in displays:
    #     print(f"{display.unique_signal_patterns} : {display.four_digit_output_values}")

    print(f"Found {sum(1 for display in displays for output in display.output_values if len(output.segments) in unique_lengths)} outputs with unique segments count")


if __name__ == '__main__':
    main()
