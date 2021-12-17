"""
@author MrNo

Summary:
Given a list of bit-strings of length n,
"""

import day3_1



def oxygen_bit_criteria(zeroes, ones):
    """
    Takes two iterables, and returns the one that is longer
    """
    return zeroes if len(zeroes) > len(ones) else ones


def co2_bit_criteria(zeroes, ones):
    """
    Takes two iterables, and returns the one that is shorter
    :param a:
    :param b:
    :return:
    """
    return zeroes if len(zeroes) <= len(ones) else ones


def divide_on_condition(inputs, condition, position=0):
    if len(inputs) == 1:
        return inputs[0]

    zeroes = []
    ones = []
    for input in inputs:
        zeroes.append(input) if input[position] == "0" else ones.append(input)

    return divide_on_condition(condition(zeroes, ones), condition, position + 1)


def main():
    filename = "inputs.txt"

    with open(filename, "r") as file:
        line_count = 0
        inputs = []
        for line in file:
            inputs.append(line.strip())

        oxygen_generator_rating = divide_on_condition(inputs, oxygen_bit_criteria)
        oxygen_decimal = int(oxygen_generator_rating, 2)
        co2_scrubber_rating = divide_on_condition(inputs, co2_bit_criteria)
        co2_decimal = int(co2_scrubber_rating, 2)

        print(f"Got\n{oxygen_generator_rating=}({oxygen_decimal})\n{co2_scrubber_rating=}({co2_decimal})\n"
              f"with product: {oxygen_decimal * co2_decimal}")


if __name__ == '__main__':
    main()
