"""
@author MrNo

Summary:
Same as day 1, except now we've discarded the "corrupted" lines and are trying to work out how to close
the "incomplete" ones.

Since this is essentially "flip the stack over", most code is copied from part 1
"""
from day10_1 import closes

error_scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

chunk_openers = ["(", "[", "{", "<"]


def main():
    autocomplete_error_scores = []
    with open("inputs.txt", "r") as file:
        for line in file:

            # this gets used like a stack
            open_chunks = []

            for index, char in enumerate(line.strip()):
                if char in chunk_openers:
                    open_chunks.append(char)
                elif closes(char, open_chunks.pop(-1)):
                    continue
                else:
                    print(f"Illegal syntax: {char} at position {index}; skipping line")
                    try:
                        # removing any leftover open chunks allows me to conveniently skip these lines
                        open_chunks = []
                        # only one error per line is counted; go to the next line
                        break
                    except KeyError:
                        raise ValueError(f"Unexpected character in input: {char}")

            score = 0
            complete = []
            while len(open_chunks) > 0:
                chunk = open_chunks.pop()
                score *= 5
                if chunk == "(":
                    complete.append(")")
                elif chunk == "[":
                    complete.append("]")
                elif chunk == "{":
                    complete.append("}")
                elif chunk == "<":
                    complete.append(">")
                score += error_scores[complete[-1]]
            if len(complete) > 0:
                print(f"Completed line with: {''.join(complete)}; score {score}")
                autocomplete_error_scores.append(score)

        autocomplete_error_scores.sort()
        print(f"Got median error score of: {autocomplete_error_scores[len(autocomplete_error_scores) // 2]}")


if __name__ == '__main__':
    main()
