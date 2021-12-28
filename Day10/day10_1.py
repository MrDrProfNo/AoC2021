"""
@author MrNo

Summary:
Look, it's a syntax parser! I loved writing these in college.
Okay, so it's a parser for a vastly simplified syntax. Basically, there are 4 different types of opening brackets, and
their corresponding closing brackets. Opened brackets can contain more opened brackets, but you have to close them in
the right order.

Some lines are "corrupted" - you get a closing bracket of the wrong type
Some lines are "incomplete" - you reach end of line before getting all closing brackets


"""

error_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

chunk_openers = ["(", "[", "{", "<"]


def closes(a: str, b: str) -> bool:
    """
    a closes b if a is the same type of bracket as b, and is the closing variant.

    If b is not an opening bracket of any type, a ValueError will be raised.

    :return: False if a is not the closing bracket for b, else True
    :raises: ValueError if b is not one of: [, {, (, <
    """

    if b == "[":
        return a == "]"
    elif b == "{":
        return a == "}"
    elif b == "(":
        return a == ")"
    elif b == "<":
        return a == ">"
    else:
        raise ValueError("Argument b must be one of: [, {, (, <")


def main():
    syntax_error_score = 0
    with open("inputs.txt", "r") as file:
        for line_number, line in enumerate(file):

            # this gets used like a stack
            open_chunks = []

            for index, char in enumerate(line.strip()):
                if char in chunk_openers:
                    open_chunks.append(char)
                elif closes(char, open_chunks.pop(-1)):
                    continue
                else:
                    print(f"Line {line_number}: Illegal syntax: {char} at position {index}")
                    try:
                        syntax_error_score += error_scores[char]

                        # only one error per line is counted; go to the next line
                        break
                    except KeyError:
                        raise ValueError(f"Unexpected character in input: {char}")

    print(f"Total syntax error score: {syntax_error_score}")


if __name__ == '__main__':
    main()
