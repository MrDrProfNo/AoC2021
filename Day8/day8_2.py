"""
@author MrNo

Summary:

"""

from display_data import DisplaySet


def main():
    with open("inputs.txt", "r") as file:
        displays = [DisplaySet(line.strip()) for line in file.readlines()]
    #
    # for display in displays:
    #     print([f"{digit} : {position}" for position, digit in enumerate(display.known_patterns)])
    #     print(f"translates to... {int(display)}")

    print(f"Sum of all displays: {sum(int(display) for display in displays)}")


    # total = 0
    # for output in outputs:
    #     total += sum(mappings[Digit(output[i])] * (10 ** (len(output)-i)) for i in range(len(output)))
    #
    # print(f"Got a total of {total} from the converted outputs")


if __name__ == '__main__':
    main()
