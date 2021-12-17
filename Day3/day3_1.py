"""
@author MrNo

Summary:
Given a list of bit-strings of length 5, create a new bit-string from the most common bits in each digit, and convert
the result to decimal. Then do it for the least common bits in each digit. Return the product of the two
"""


def main():
    filename = "inputs.txt"
    with open(filename, "r") as file:
        line_count = 0
        sums = [0 for _ in range(12)]
        for line in file:
            sum_indices = range(len(sums))
            for index in sum_indices:
                sums[index] += int(line[index])
            line_count += 1

        gamma_rate = [sum > (line_count // 2) for sum in sums]
        gamma_rate_decimal = bits_to_int(gamma_rate)
        epsilon_rate = [not gamma_rate[index] for index in range(len(gamma_rate))]
        epsilon_rate_decimal = bits_to_int(epsilon_rate)

        print(f"Got\n{gamma_rate=}({gamma_rate_decimal})\n{epsilon_rate=}({epsilon_rate_decimal})\n"
              f"with product: {gamma_rate_decimal * epsilon_rate_decimal}")


def bits_to_int(bitarray):
    out = 0
    for index, bit in enumerate(bitarray):
        # the -1 is necessary because you want the first bit left shifted to the leftmost extreme, but it's at 1
        out = (bit << (len(bitarray) - index - 1)) | out
    return out


if __name__ == '__main__':
    main()
